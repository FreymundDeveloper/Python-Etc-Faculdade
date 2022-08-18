#!/usr/bin/env python

from math import atan2, sqrt
import math
from turtle import pos
from move_quadrado import publisher
import rospy
from geometry_msgs.msg import Twist
import sys
import os
import kbhit
import time
from turtlesim.msg import Pose

feedback = Pose()

def subCallback(msg):
    feedback.x = msg.x
    feedback.y = msg.y
    feedback.theta = msg.theta

def publisher():
    rospy.init_node('turtle_controle_posicao', anonymous=True)
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber("turtle1/pose", Pose, subCallback)

    rate = rospy.Rate(10)

    msg = Twist()
    posdesejada = []
    dist = 99
    erroorie = 99
    tolerance_orie = 0.005
    tolerance_pos = 0.05
    kpos = 1.5
    korie = 4

    os.system('rosservice call /reset')

    posdesejada.append(float(input('Posicao X: ')))
    posdesejada.append(float(input('Posicao Y: ')))

    angulo = math.atan2(posdesejada[1] - feedback.y, posdesejada[0] - feedback.x)

    while abs(erroorie) > tolerance_orie:
        erroorie = angulo - feedback.theta
        msg.angular.z = korie * erroorie
        rospy.loginfo("theta>>%f,Erro>>%f",feedback.theta,erroorie)
        pub.publish(msg)
        rate.sleep()

    msg.angular.z = 0
    pub.publish(msg)

    while dist > tolerance_pos:
        dist = math.sqrt(math.pow(posdesejada[0] - feedback.x,2) + math.pow(posdesejada[1] - feedback.y,2))
        msg.linear.x = abs(kpos * (dist))
        rospy.loginfo("Dist>>%f",dist)
        pub.publish(msg)
        rate.sleep()

    msg.linear.x = 0
    pub.publish(msg)

    rospy.loginfo("Chegou!!!")

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass