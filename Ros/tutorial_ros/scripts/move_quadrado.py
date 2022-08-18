#!/usr/bin/env python
## Movimento quadrado

import rospy
from geometry_msgs.msg import Twist
import math, os
import time
import sys

def publisher():
    rospy.init_node('turtle_movimento_quadrado', anonymous=True)
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    go = Twist()

    rospy.loginfo("Pressioe qualquer teclo para iniciar...")
    os.system('rosservice call /reset')
    c = sys.stdin.read(1)


    for i in range(4):
        go.linear.x = 2
        go.angular.z = 0
        rospy.sleep(2)
        pub.publish(go)

        go.linear.x = 0
        go.angular.z = math.pi / 2
        rospy.sleep(2)
        pub.publish(go)

    #while not rospy.is_shutdown():

        #for i in range(4):
         #   go.linear.x = 2 
          #  go.angular.z = 0 
           # start = time.time()

            #while((time.time() - start) < 2):

            #   if((time.time() - start) > 1):
             #       go.linear.x = 0
              #      go.angular.z = math.pi / 2
                
               # pub.publish(go)

        #go.linear.x = 0.3
        #go.angular.z = 0
        #pub.publish(go)
        #break

    rospy.loginfo('Quadrado finalizado...')


if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass