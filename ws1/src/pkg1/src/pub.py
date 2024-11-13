#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def talker():
    pub = rospy.Publisher('count', Int32)
    rospy.init_node('pub')
    rate = rospy.Rate(1)  # 1 Hz

    count = 0
    while not rospy.is_shutdown():
        print("Publishing: %d", count)
        pub.publish(count)
        count += 1
        rate.sleep()

if __name__ == '__main__':
        talker()

