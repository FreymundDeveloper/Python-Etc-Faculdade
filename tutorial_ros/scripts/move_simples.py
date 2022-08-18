#!/usr/bin/env python
## Movimento simples

import rospy
from geometry_msgs.msg import Twist
import time
import sys
import os

def publisher():
    rospy.init_node('turtle_movimento_simples', anonymous=True)
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    go = Twist()

    rospy.loginfo("Pressioe qualquer teclo para iniciar...")
    os.system('rosservice call /reset')
    c = sys.stdin.read(1)

    go.linear.x = 2
    go.angular.z = 0
    rospy.sleep(1)
    pub.publish(go)

    rospy.sleep(2)
    go.linear.x = 0
    pub.publish(go)

    #while not rospy.is_shutdown():
        #go.linear.x = 2 
        #start = time.time()

        #while((time.time() - start) < 2):
            #pub.publish(go)

        #go.linear.x = 0
        #pub.publish(go)
        #break

    #rospy.loginfo('Trajeto finalizado...')

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass

