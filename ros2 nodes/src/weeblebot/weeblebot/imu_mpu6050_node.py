#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2020-02-11

@author: Peter Adamczyk
updated 2025-02-27
"""

from weeblebot.mpu6050 import mpu6050
import traceback
import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu

class IMUNode(Node):

    def __init__(self):
        super().__init__('imu_mpu6050_node')
        self.pub_imu = self.create_publisher(Imu, '/imu_mpu6050', 1)
        self.timer = self.create_timer(0.05, self.read_imu)
        self.imu = mpu6050(0x68)
        self.imu.set_accel_range(self.imu.ACCEL_RANGE_4G)
        self.imu.set_gyro_range(self.imu.GYRO_RANGE_1000DEG)
        self.imu.calibrateGyro(500)
        self.counter = 0

    def read_imu(self):
        imu_msg = Imu()
        accel, gyro, _ = self.imu.get_all_data()
        self.counter += 1

        imu_msg.header.seq = self.counter
        imu_msg.header.stamp = rclpy.get_clock().now()
        imu_msg.header.frame_id = 'imu'
        imu_msg.orientation.x = 0.
        imu_msg.orientation.y = 0.
        imu_msg.orientation.z = 0.
        imu_msg.orientation.w = 0.
        imu_msg.orientation_covariance = np.array(
            [0.,0.,0.,
             0.,0.,0.,
             0.,0.,0.])
        imu_msg.angular_velocity.x = gyro['x']*3.1415926/180
        imu_msg.angular_velocity.y = gyro['y']*3.1415926/180
        imu_msg.angular_velocity.z = gyro['z']*3.1415926/180
        imu_msg.angular_velocity_covariance = np.array(
            [0.,0.,0.,
             0.,0.,0.,
             0.,0.,0.])
        imu_msg.linear_acceleration.x = accel['x']
        imu_msg.linear_acceleration.y = accel['y']
        imu_msg.linear_acceleration.z = accel['z']
        imu_msg.linear_acceleration_covariance = np.array(
            [0.,0.,0.,
             0.,0.,0.,
             0.,0.,0.])

        self.pub_imu.publish(imu_msg)



def main(args=None):
    try: 
        rclpy.init(args=args)
        imu_mpu6050_node = IMUNode()
        rclpy.spin(imu_mpu6050_node)
        
    except: 
        traceback.print_exc()

if __name__ == '__main__':
    main()