#!/usr/bin/env python
import rospy
from pkg5.srv import fserv

if __name__ == '__main__':
	rospy.init_node('clt') 
	rospy.wait_for_service('topic2')
       
    
	
	cl = rospy.ServiceProxy('topic2', fserv)

	
	X = 50
	Y = 60

	
	r = cl(X, Y)

	rospy.loginfo('amir...{}'.format(r.mean))
