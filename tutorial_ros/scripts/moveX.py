#!/usr/bin/env python

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
    rospy.init_node('turtle_controle_X', anonymous=True)
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber("turtle1/pose", Pose, subCallback)

    rate = rospy.Rate(10)

    os.system('rosservice call /reset')

    msg = Twist()
    desejado = float(input("Digita o lugar: "))
    tolerance = 0.01
    erro = 99
    kp = 1.5


    while abs(erro) > tolerance:
        erro = desejado - feedback.x
        msg.linear.x = kp * erro
        rospy.loginfo("X>>%f,Erro>>%f",feedback.x,erro)
        pub.publish(msg)
        rate.sleep()
    
    rospy.loginfo("Chegou!!!")

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass