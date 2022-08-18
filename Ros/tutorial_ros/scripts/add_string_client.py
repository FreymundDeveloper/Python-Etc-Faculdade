#!/usr/bin/env python
import sys
import rospy
from tutorial_ros.srv import *

def add_string_client(x):
	rospy.wait_for_service('add_string')
	try:
			add_string = rospy.ServiceProxy('add_string', Liga_Desliga)
			resp1 = add_string(x)
			return resp1.sum
	except rospy.ServiceException as e:
			print("Service call failed: %s"%e)
def usage():
    	return "%s [x]"%sys.argv[0]

if __name__ == "__main__":
	if len(sys.argv) == 2:
			x = int(sys.argv[1])
	else:
			print(usage())
			sys.exit(1)
	print("Requesting", x)
	print("%s = %s"%(x, add_string_client(x)))