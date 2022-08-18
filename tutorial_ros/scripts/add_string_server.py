#!/usr/bin/env python
from tutorial_ros.srv import Liga_Desliga,Liga_DesligaResponse 
import rospy 

def handle_string(req):
    if req.a == 0:
        status = 'desligado'
    elif req.a == 1:
        status = 'ligado'
    else:
        status = 'not right'
        
    print("Returning [%s = %s]"%(req.a, status))
    return Liga_DesligaResponse(status)
	
def add_string_server():
	rospy.init_node('add_string_server')
	s = rospy.Service('add_string', Liga_Desliga, handle_string)
	print("Ready to add string.")
	rospy.spin() 
if __name__ == "__main__":
    add_string_server()