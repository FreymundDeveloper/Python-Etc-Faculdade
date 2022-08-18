#!/usr/bin/env python

import math
from turtle import position
import rospy
from geometry_msgs.msg import Twist
import sys
import os
import time
from turtlesim.msg import Pose
from dijkstra import Graph

feedback = Pose()

def subCallback(msg):
    feedback.x = msg.x
    feedback.y = msg.y
    feedback.theta = msg.theta

def publisher():
    rospy.init_node('turtle_controle_pid', anonymous=True)

    os.system('rosservice call /reset')
    os.system('rosservice call /kill turtle1')

    os.system("rosservice call /spawn 1.0 1.0 0.0 turtle1")
    os.system("rosservice call /turtle1/set_pen 255 0 0 4 0")

    os.system("rosservice call /spawn 6.0 1.0 0.0 turtle2")
    os.system("rosservice call /turtle2/teleport_absolute 6.0 1.0 0.0")
    os.system("rosservice call /turtle2/set_pen 0 255 0 4 0")

    turtle = int(input('Turtle 1 ou 2: ')) 

    letra = raw_input('Qual a letra desejada. A, B, C ou D: ')

    if turtle == 1:
        x = y = 1

    else:
        x = 6
        y = 1

    if letra == 'A':
        g = Graph(5)
        g.graph = [[0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]
        precedente = g.dijkstra(0)
        pontos = [[x, y], [x+2, y+4], [x+4, y], [x+3.2, y+2], [x+0.7, y+2]]

    elif letra == 'B':
        g = Graph(6)
        g.graph = [[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]
        precedente = g.dijkstra(0)
        pontos = [[x, y], [x, y+6], [x+2, y+4], [x, y+3], [x+3, y+1], [x, y]]

    elif letra == 'C':
        if turtle == 1:
            x = 5
            y = 2
            os.system("rosservice call /turtle1/teleport_absolute 5.0 2.0 0.0")
            os.system('rosservice call /clear')
        else:
            x = 10
            y = 2
            os.system("rosservice call /turtle2/teleport_absolute 10.0 2.0 0.0")
            os.system('rosservice call /clear')


        g = Graph(5)
        g.graph = [[0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]
        precedente = g.dijkstra(0)
        pontos = [[x, y], [x-3, y-1], [x-5, y+2], [x-3, y+4], [x, y+3]]

    elif letra == 'D':
        g = Graph(6)
        g.graph = [[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]
        precedente = g.dijkstra(0)
        pontos = [[x, y], [x, y+6], [x+2, y+4], [x+2.5, y+3], [x+2, y+2], [x, y]]

    mapeamento = []
    while len(precedente) > 0:
        localizacao = precedente.pop()
        mapeamento.insert(0, pontos[localizacao])
    mapeamento.pop(0)
    mapeamento.append(pontos[-1])

    for p in mapeamento:
        turtle_map(turtle, posicao = p)

def turtle_map(turtle, posicao):
    rate = rospy.Rate(10)

    x = posicao[0]
    y = posicao[1]

    msg = Twist()
    error = 99
    erroorie = 0
    errorInt = 0
    lastError = 0

    tolerance_orie = 0.005
    tolerance_pos = 0.05
    kpos = 0.75
    ki = 0.000001
    kd = 0.000001
    korie = 10
    last_time = None

    pub = rospy.Publisher('turtle%i/cmd_vel' % turtle, Twist, queue_size=10)
    sub = rospy.Subscriber("turtle%i/pose" % turtle, Pose, subCallback)


    pose_atual = rospy.wait_for_message('/turtle%i/pose' % turtle, Pose)
    subCallback(pose_atual)

    while abs(erroorie) > tolerance_orie or abs(error) > tolerance_pos:
        if last_time is None:
            last_time = rospy.get_time()
        
        actual_time = rospy.get_time()
        dt = actual_time - last_time
        lastError = error

        angulo = math.atan2(y - feedback.y, x - feedback.x)

        erroorie = angulo - feedback.theta
        msg.angular.z = korie * erroorie
        rospy.loginfo("theta>>%f,Erro>>%f",feedback.theta,erroorie)

        error = math.sqrt(math.pow(x - feedback.x,2) + math.pow(y - feedback.y,2))
        errorInt = errorInt + (error * dt)
        errorDer = (error - lastError) / dt
        msg.linear.x = kpos * error + ki * errorInt + kd * errorDer
        rospy.loginfo("Dist>>%f",error)
        #last_time = actual_time
        pub.publish(msg)
        rate.sleep()

    msg.angular.z = 0
    msg.linear.x = 0
    pub.publish(msg)

    rospy.loginfo("Chegou!!!")

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass