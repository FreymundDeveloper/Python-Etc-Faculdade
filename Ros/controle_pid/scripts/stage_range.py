#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

rng = 2.0

def callback(msg):
    global rng
    rng = msg.ranges[0] 
    

def publisher():
    rospy.init_node('stage_range_pid', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber('/base_scan', LaserScan, callback)

    rate = rospy.Rate(10)
    msg = Twist()

    while True:
        msg.linear.x = 1
        msg.angular.z = 0

        if rng < 2:
            msg.linear.x -= 0.5
            msg.angular.z -= 1 

        if rng >= 2:
            msg.linear.x = 1
            msg.angular.z = 0

        pub.publish(msg)
        rate.sleep()
   

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass