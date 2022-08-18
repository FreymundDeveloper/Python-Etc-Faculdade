#!/usr/bin/env python

import rospy
import time
from tutorial_ros.msg import Num
from geometry_msgs.msg import Twist

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data)
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    publisher(data.num, pub)

def publisher(x, pub):
    go = Twist()
    go.linear.x = x

    time.sleep(1)
    pub.publish(go)
    time.sleep(1)

    go.linear.x = 0
    pub.publish(go)

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('turtle_opcao', Num, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()