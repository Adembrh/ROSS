#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
import numpy as np
def call(t):
	print(t.data)


if __name__=='__main__':
	rospy.init_node('sub')
	rospy.Subscriber('topic1',Int32,call)
	
        
	rospy.spin()
        
        
	
	
	
