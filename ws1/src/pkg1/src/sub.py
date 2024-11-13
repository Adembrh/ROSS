#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def callback(data):
    
    print("Received: %d", data.data)
def listener():
    rospy.init_node('sub')
    rospy.Subscriber('count', Int32, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

