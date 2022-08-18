#!/usr/bin/env python

import math
import rospy
from geometry_msgs.msg import Twist
import sys
import os
import time
from turtlesim.msg import Pose

feedback = Pose()

def subCallback(msg):
    feedback.x = msg.x
    feedback.y = msg.y
    feedback.theta = msg.theta

def publisher():
    rospy.init_node('turtle_controle_pid', anonymous=True)
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber("turtle1/pose", Pose, subCallback)

    rate = rospy.Rate(10)

    msg = Twist()
    posdesejada = []
    error = 99
    erroorie = 0
    errorInt = 0
    lastError = 0

    tolerance_orie = 0.005
    tolerance_pos = 0.05
    kpos = 0.75
    ki = 0.000001
    kd = 0.000005
    korie = 6
    last_time = None

    os.system('rosservice call /reset')

    posdesejada.append(float(input('Posicao X: ')))
    posdesejada.append(float(input('Posicao Y: ')))

    pose_atual = rospy.wait_for_message('/turtle1/pose', Pose)
    subCallback(pose_atual)

    while abs(erroorie) > tolerance_orie or abs(error) > tolerance_pos:
        if last_time is None:
            last_time = rospy.get_time()
        
        actual_time = rospy.get_time()
        dt = actual_time - last_time
        lastError = error

        angulo = math.atan2(posdesejada[1] - feedback.y, posdesejada[0] - feedback.x)

        erroorie = angulo - feedback.theta
        msg.angular.z = korie * erroorie
        rospy.loginfo("theta>>%f,Erro>>%f",feedback.theta,erroorie)

        error = math.sqrt(math.pow(posdesejada[0] - feedback.x,2) + math.pow(posdesejada[1] - feedback.y,2))
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