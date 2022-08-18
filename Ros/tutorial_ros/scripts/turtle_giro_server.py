#!/usr/bin/env python
from tutorial_ros.srv import Liga_Desliga,Liga_DesligaResponse 
import rospy
from geometry_msgs.msg import Twist
import sys 
import os

def publisher(opc):
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    go = Twist()

    if opc == 0:
        os.system('rosservice call /reset')

    elif opc == 1:
        go.linear.x = 10
        go.angular.z = 6.2

        rospy.sleep(1)
        pub.publish(go)
        rospy.sleep(1)

def handle_turtle_giro(req):
    if req.a == 0:
        status = 'limpar tela'
        publisher(0)
    elif req.a == 1:
        status = 'Girar tutle'
        publisher(1)
    else:
        status = 'not right'
        
    print("Returning [%s = %s]"%(req.a, status))
    return Liga_DesligaResponse(status)
	
def add_turtle_giro_server():
	rospy.init_node('add_turtle_giro_server')
	s = rospy.Service('add_return', Liga_Desliga, handle_turtle_giro)
	print("Ready to go.")
	rospy.spin() 
if __name__ == "__main__":
    add_turtle_giro_server()