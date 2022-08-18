#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

ranged1= [5]
ranged2= [5]
ranged3= [5]

def callback(msg):
    global ranged1 
    global ranged2 
    global ranged3

    ranged1 = msg.ranges[0:29] #direito
    ranged2 = msg.ranges[30:59] #meio
    ranged3 = msg.ranges[60:89] #esquerdo
    

def publisher():
    rospy.init_node('stage_range_pid', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber('/base_scan', LaserScan, callback)

    rate = rospy.Rate(10)
    msg = Twist()

    while True:
        msg.linear.x = 1
        msg.angular.z = 0

        min1 = min(ranged1)
        min2 = min(ranged2)
        min3 = min(ranged3)

        if min1 < 1 or min2 < 1 or min3 < 1:
            if min1 < 1:
                msg.linear.x = 0.5
                msg.angular.z = 1 

            elif min2 < 1:
                msg.linear.x = 0.1

                if min1 < 1.2:
                    msg.angular.z = 1 

                elif min3 < 1.2:
                    msg.angular.z = -1 
                

            elif min3 < 1:
                msg.linear.x = 0.5
                msg.angular.z = -1 


        pub.publish(msg)
        rate.sleep()
   

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass