#!/usr/bin/env python

import math
import rospy
from geometry_msgs.msg import Twist
import os
from turtlesim.msg import Pose
import tf
from tf.transformations import euler_from_quaternion
from nav_msgs.msg import Odometry

feedback = Pose()

def callback(msg):
    feedback.x = msg.pose.pose.position.x # posicao x do robo no mundo
    feedback.y = msg.pose.pose.position.y # posicao y do robo no mundo
    x_q = msg.pose.pose.orientation.x
    y_q = msg.pose.pose.orientation.y
    z_q = msg.pose.pose.orientation.z
    w_q = msg.pose.pose.orientation.w
    euler = euler_from_quaternion ([x_q , y_q , z_q , w_q ])
    feedback.theta = euler [2] # orientacao theta do robo no mundo
    ##rospy.loginfo('I heard x %f y %f ', feedback.x, feedback.y)

def publisher():
    rospy.init_node('stage_controle_pid', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber('/base_pose_ground_truth', Odometry, callback)

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

    ##os.system('rosservice call /reset')

    posdesejada.append(float(input('Posicao X: ')))
    posdesejada.append(float(input('Posicao Y: ')))

    while abs(erroorie) > tolerance_orie or abs(error) > tolerance_pos:
        if last_time is None:
            last_time = rospy.get_time()
        
        actual_time = rospy.get_time()
        dt = actual_time - last_time
        lastError = error

        if dt == 0:
            dt = 1

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