#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################
# Aula 26/09/2022
######################


## 
## Desenvolva um pacote compatível com o Robot
## Operating System (ROS) para a movimentação de
## um robô móvel utilizando o ambiente CoppeliaSim;
## • A estratégia deve permitir que o robô movimente-se
## constantemente para frente, desviando de todos os
## obstáculos detectados pela forma de percepção
## LIDAR;
## • Deve-se empregar uma estratégia Fuzzy para o
## desvio.
## 

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import Joy
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def control(precision=0.1):
	distancia = ctrl.Antecedent(np.arange(0, 1.5, precision), "distancia")
	distancia["Perto"] = fuzz.trapmf(distancia.universe, [-0.7, -0.6, 0, 0.4])
	distancia["Moderado"] = fuzz.trimf(distancia.universe, [0.3, 0.55, 0.8])
	distancia["Longe"] = fuzz.trapmf(distancia.universe, [0.7, 1.2, 1.6, 2])
	direcao = ctrl.Antecedent(np.arange(0, 511, precision), "direcao")
	direcao["Direita"] = fuzz.trapmf(direcao.universe, [-192, -21.3, 150, 190])
	direcao["Centro"] = fuzz.trimf(direcao.universe, [160, 255, 350])
	direcao["Esquerda"] = fuzz.trapmf(direcao.universe, [320, 360, 532.3, 702.6])
	velLinear = ctrl.Consequent(np.arange(0, 3 , precision), "velLinear")
	velLinear["Devagar"] = fuzz.trapmf(velLinear.universe, [-0.4, -0.1, 0.1, 0.3])
	velLinear["Moderado"] = fuzz.trimf(velLinear.universe, [0.2, 0.75, 1.25])
	velLinear["Veloz"] = fuzz.trapmf(velLinear.universe, [1.0, 1.5, 3.1, 3.2])
	velAngular = ctrl.Consequent(np.arange(-7, 7 , precision), "velAngular")
	velAngular["viraMuitoDireita"] = fuzz.trapmf(velAngular.universe, [-12, -11, -5, -3])
	velAngular["viraDireita"] = fuzz.trimf(velAngular.universe, [-4, -2, 0])
	velAngular["Reto"] = fuzz.trimf(velAngular.universe, [-0.5, 0, 0.5])
	velAngular["viraEsquerda"] = fuzz.trimf(velAngular.universe, [0, 2, 4])
	velAngular["viraMuitoEsquerda"] = fuzz.trapmf(velAngular.universe, [3, 5, 11, 12])

	regra1 = ctrl.Rule((distancia [ "Perto" ] & direcao [ "Direita" ]),(velLinear [ "Devagar" ], velAngular [ "viraMuitoEsquerda" ]))

	regra2 = ctrl.Rule((distancia [ "Perto" ] & direcao [ "Centro" ]),(velLinear [ "Devagar" ], velAngular [ "viraMuitoDireita" ]))

	regra3 = ctrl.Rule((distancia [ "Perto" ] & direcao [ "Esquerda" ]),(velLinear [ "Devagar" ], velAngular [ "viraMuitoDireita" ]))

	regra4 = ctrl.Rule((distancia [ "Moderado" ] & direcao [ "Direita" ]),(velLinear [ "Moderado" ], velAngular [ "viraEsquerda" ]))

	regra5 = ctrl.Rule((distancia [ "Moderado" ] & direcao [ "Centro" ]),(velLinear [ "Moderado" ], velAngular [ "Reto" ]))

	regra6 = ctrl.Rule((distancia [ "Moderado" ] & direcao [ "Esquerda" ]),(velLinear [ "Moderado" ], velAngular [ "viraDireita" ]))

	regra7 = ctrl.Rule((distancia [ "Longe" ] & direcao [ "Direita" ]),(velLinear [ "Veloz" ], velAngular [ "Reto" ]))

	regra8 = ctrl.Rule((distancia [ "Longe" ] & direcao [ "Centro" ]),(velLinear [ "Veloz" ], velAngular [ "Reto" ]))

	regra9 = ctrl.Rule((distancia [ "Longe" ] & direcao [ "Esquerda" ]),(velLinear [ "Veloz" ], velAngular [ "Reto" ]))

	c_ctrl = ctrl.ControlSystem([regra1, regra2, regra3, regra4, regra5, regra6, regra7, regra8, regra9])

	return ctrl.ControlSystemSimulation(c_ctrl)

ranges = []
axes = []
# right_side = ranges[0:169]
# center = ranges[170:339]
# left_side = ranges[340:511]

def baseScanCallback(data):
    global ranges
    ranges = data.ranges
    # rospy.loginfo('Ranges>>%s' % str(ranges))

def JoyCallback(data):
    global axes
    axes = data.axes
    

def main():
    rospy.init_node('fuzzy_laser', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber('/scan', LaserScan, callback=baseScanCallback)
    sub2 = rospy.Subscriber('/joy', Joy, callback=JoyCallback)
    
    rate = rospy.Rate(10)

    msg = Twist()
    
    while True:

        if len(ranges) > 0:
            min_all = 99999999
            min_index = -1
            index = 0
            for value in ranges:
                if value < min_all:
                    min_all = value
                    min_index = index
                index += 1

            if min_all < 0.4:
                tipping = control()

                print('direcao: %d // distancia: %d' % (min_index, min_all))
                tipping.input['direcao'] = min_index
                tipping.input['distancia'] = min_all
                
                
                tipping.compute()

                msg.angular.z = tipping.output['velAngular']
                msg.linear.x = tipping.output['velLinear']

            else:
                if len(axes) > 2:
                    msg.linear.x = axes[1] * 2
                    msg.angular.z = axes[0] * 5 

        pub.publish(msg)
        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass