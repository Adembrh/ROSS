#!/usr/bin/env python
import rospy
from pkg5.srv import fserv, fservResponse  

def amir(t):
    
    mean = (t.a + t.b) / 2
    
    return fservResponse(mean)

if __name__ == '__main__':
    rospy.init_node('serv')  
    
    rospy.Service('topic2', fserv, amir)
    
    
    rospy.spin() 

