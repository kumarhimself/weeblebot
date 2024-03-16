#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2020-02-11

@author: Peter Adamczyk
"""
# modified to use the sparkfun icm20948 imu

import qwiic_icm20948 as icm
import time
import traceback
import numpy as np
import rospy
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Quaternion



def imu_talker():
    rospy.init_node('imu_icm20948_node',anonymous=False)
    
    # Publisher
    imu_pub = rospy.Publisher('/imu_raw',Imu,queue_size=1)
    
    # Message
    imu_msg = Imu()
    
    # set a Rate at which it should be read
    r = rospy.Rate(50)
    imu = icm.QwiicIcm20948()
    imu.begin()
    imu.setFullScaleRangeAccel(icm.gpm4)
    imu.setFullScaleRangeGyro(icm.dps1000)
    imu.enableDlpfAccel(True)
    imu.enableDlpfGyro(True)

    counter = 0
    
    # dummy code to print values for a while
    while not rospy.is_shutdown():
        imu.getAgmt()
        counter += 1
#        # this will print the data that are returned
        #print('a: {0}, w: {1}, T: {2}'.format(accel, gyro, temp))
#        rospy.loginfo('a: {0}, w: {1}, T: {2}'.format(accel, gyro, temp))
        
        # Pack the message
        imu_msg.header.seq = counter
        imu_msg.header.stamp = rospy.get_rostime()
        imu_msg.header.frame_id = ''
        imu_msg.orientation.x = 0.
        imu_msg.orientation.y = 0.
        imu_msg.orientation.z = 0.
        imu_msg.orientation.w = 0.
        imu_msg.orientation_covariance = np.array([-1,0.,0.,0.,0.,0.,0.,0.,0.])
        imu_msg.angular_velocity.x = imu.gxRaw*3.1415926/180
        imu_msg.angular_velocity.y = imu.gyRaw*3.1415926/180
        imu_msg.angular_velocity.z = imu.gzRaw*3.1415926/180
        imu_msg.angular_velocity_covariance = np.array([0.,0.,0.,0.,0.,0.,0.,0.,0.])
        imu_msg.linear_acceleration.x = imu.axRaw/100
        imu_msg.linear_acceleration.y = imu.ayRaw/100
        imu_msg.linear_acceleration.z = imu.azRaw/100
        imu_msg.linear_acceleration_covariance = np.array([0.,0.,0.,0.,0.,0.,0.,0.,0.])
        
        imu_pub.publish(imu_msg) 
        
        r.sleep()
        
        
    
# the system literal "__name__" will be "__main__" if the user launches this file. 
# In that case, run the main program. 
# Otherwise it will be something related to whatever program called this one.     
if __name__ == "__main__":
    try:
        imu_talker()
    except rospy.ROSInterruptException: 
        traceback.print_exc()
        pass
