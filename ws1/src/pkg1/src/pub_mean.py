#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray  # Correct message type
from std_msgs.msg import Int32
import numpy as np

if __name__ == '__main__':
    rospy.init_node('pub_mean')
    pub = rospy.Publisher('topic1', Float32MultiArray, queue_size=10)  # Corrected message type and added queue_size
    rate = rospy.Rate(0.1)
    
    x = np.matrix([[1, 2], [4, 3]])
    mean = (x.sum()) / x.size  # Calculate the mean

    # Initialize Float32MultiArray and set the data field
    mmean = Float32MultiArray()
    mmean.data = [mean]  # Set mean as a single-element list to match Float32MultiArray format

    while not rospy.is_shutdown():
        pub.publish(mmean)  # Publish the message
        rospy.loginfo("Publishedmean{}".format(mmean.data))
        rate.sleep()
