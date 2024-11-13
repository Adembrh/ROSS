#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray

def callback(v):
	rospy.loginfo('received{}'.format(v.data))
if __name__=='__main__':
	rospy.init_node('sub_mean')
	rospy.Subscriber('topic1',Float32MultiArray,callback)
	rospy.spin()
