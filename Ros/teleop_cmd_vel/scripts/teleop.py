#!/usr/bin/env python
## Movimento quadrado

import rospy
from geometry_msgs.msg import Twist
import os
import time
import kbhit

def publisher(x, z, pub):
    go = Twist()
    go.linear.x = x
    go.angular.z = z
    pub.publish(go)



def menu():
    rospy.loginfo("Menu\nW - Movimento linear para frente\nX - Movimento linear para tras\nA - Movimento angular anti-horario\n"
    "D - Movimento angular horario\nQ - Movimento linear para frente com giro anti-horario\nZ - Movimento linear para tras com giro anti-horario\n"
    "E - Movimento linear para frente com giro horario\nC - Movimento linear para tras com giro horario\n"
    "S - Parado\n1 - Incrementa a velocidade linear\n2 - Decrementa a velocidade linear\n3 - Incrementa a velocidade angular\n"
    "4 - Decrementa a velocidade angular\nP - Fecha o no")

def master():
    rospy.init_node('turtle_move', anonymous=True)
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)

    os.system('rosservice call /reset')

    kbhit.init()
    menu()

    velLinear = 0.5
    velAngular = 0.5
    incremento = 0.1
    

    while True:
        if kbhit.kbhit():
            ch = kbhit.getch()
            rospy.loginfo("Opcao: %s",ch)
            if ch.upper() == 'W':
                publisher(velLinear, 0, pub)
            elif ch.upper() == 'X':
                publisher(-velLinear, 0, pub)
            elif ch.upper() == 'A':
                publisher(0, velAngular, pub)
            elif ch.upper() == 'D':
                publisher(0, -velAngular, pub)
            elif ch.upper() == 'Q':
                publisher(velLinear, velAngular, pub)
            elif ch.upper() == 'Z':
                publisher(-velLinear, velAngular, pub)
            elif ch.upper() == 'E':
                publisher(velLinear, -velAngular, pub)
            elif ch.upper() == 'C':
                publisher(-velLinear, -velAngular, pub)
            elif ch.upper() == 'S':
                publisher(0, 0, pub)
            elif ch.upper() == '1':
                velLinear += incremento
            elif ch.upper() == '2':
                velLinear -= incremento
            elif ch.upper() == '3':
                velAngular += incremento
            elif ch.upper() == '4':
                velAngular -= incremento
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