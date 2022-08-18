#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32

rng = 2.0

def callback(msg):
    global rng
    rng = msg.data
    

def publisher():
    rospy.init_node('stage_range_pid', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber('/ultrassom', Float32, callback)

    rate = rospy.Rate(10)
    msg = Twist()

    while True:
        msg.linear.x = 1
        msg.angular.z = 0

        if rng < 2 and rng > 0:
            if rng < 1:
                msg.linear.x = 0.1
                msg.angular.z -= 6
                
            else:    
                msg.linear.x -= 0.5
                msg.angular.z -= 6 

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