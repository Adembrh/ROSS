#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32
import numpy as np
if __name__=='__main__':
	rospy.init_node('pub')
	pub=rospy.Publisher('topic1',Int32)
	x = np.matrix([[1, 2], [4, 3]])
	maxi=x[0,0]
	rate=rospy.Rate(10)
	
	for i in range(2):
        	for j in range(2):
        		if x[i,j] > maxi:
            			maxi = x[i,j]
	while not rospy.is_shutdown():
        	pub.publish(int(maxi))
        	print(maxi)
        	rate.sleep()
        
        
        
	
	
	
