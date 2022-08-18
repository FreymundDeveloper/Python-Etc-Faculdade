#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import os
import time
import kbhit
from tutorial_ros.msg import Num

def publisher(x, pub):
    pub.publish(x)


def menu():
    rospy.loginfo("Menu:\n1 - Velocidade 1.0\n2 - Velocidade 2.0\n3 - velocidade 3.0")

def master():
    rospy.init_node('turtle_msg', anonymous=True)
    pub = rospy.Publisher('turtle_opcao', Num, queue_size=10)

    os.system('rosservice call /reset')

    kbhit.init()
    menu()
    

    while True:
        if kbhit.kbhit():
            ch = kbhit.getch()
            rospy.loginfo("Opcao: %s",ch)
            if ch.upper() == '1':
                publisher(1.0, pub)
            elif ch.upper() == '2':
                publisher(2.0, pub)
            elif ch.upper() == '3':
                publisher(3.0, pub)
            elif ch.upper() == 'P':
                break
            else:
                rospy.loginfo('Comando INVALIDO')
            menu()
            time.sleep(0.1)

    kbhit.restore()

    rospy.loginfo('Programa finalizado...')


if __name__ == '__main__':
    try:
        master()
    except rospy.ROSInterruptException:
        pass