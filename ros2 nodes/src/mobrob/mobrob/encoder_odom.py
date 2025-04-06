#!/usr/bin/env python3

# =============================================================================
# Peter G. Adamczyk 
# Updated 2024-10-11
# Updated 2025-03-06
# =============================================================================


import rclpy
from rclpy.node import Node
import numpy as np
import traceback 
from geometry_msgs.msg import Pose2D, Quaternion
from nav_msgs.msg import Odometry
from mobrob_interfaces.msg import ME439WheelDisplacements

    
class WheelOdom(Node): 
    def __init__(self):
        super().__init__('wheel_odom')

        # Variables for the robot's wheel displacements (to keep knowledge of it from one step to the next)
        self.d_left_previous = 0.
        self.d_right_previous = 0.
        self.time_prev = self.get_clock().now().nanoseconds

        self.theta_est = 0.
        self.position_est = np.array([0.,0.])
        self.speed = 0.
        self.spin_rate = 0.
        self.orientation_est = 0.
        # Rate to set how often the estimated "pose" is published
        self.freq = 10.     # Hz 
        #==============================================================================
        # # Get parameters from rosparam
        # # NOTE this is the Estimator, so we should use the "model" parameters. 
        # # This will enable us to compare the "simulated" robot (considered the true robot location) 
        # #  and the "estimated" robot (position estimated based on dead-reckoning)
        #==============================================================================
        self.wheel_width = self.declare_parameter('/wheel_width', 0.584).value
    
        self.sub_wheel_disps = self.create_subscription( ME439WheelDisplacements, '/wheel_displacements', self.wheel_odom, 1 )  
            
        self.pub_robot_odom_estimated = self.create_publisher(Odometry, 'odometry/wheels', 1)

        # =============================================================================
        #     # Timer to set a publication rate. This calls a publication callback
        # =============================================================================
        self.pub_timer = self.create_timer(1.0/self.freq, self.pub_callback)
    
    # =============================================================================
    #     # Callback to do the publication
    #     # This function is called by the timer above at a constant rate. Its job is to publish the current estimate of the robot pose. 
    # =============================================================================
    def pub_callback(self): 
        # Pack the message
        odom_estimated_msg = Odometry()
        odom_estimated_msg.header.stamp = self.get_clock().now().to_msg()
        odom_estimated_msg.header.frame_id = 'odom' # fixed world frame
        odom_estimated_msg.child_frame_id = 'base_link' # frame of the robot base link
        odom_estimated_msg.twist.twist.linear.x = self.speed
        odom_estimated_msg.twist.twist.linear.y = 0. #TODO: make this consider strafing
        odom_estimated_msg.twist.twist.angular.z = self.spin_rate
        odom_estimated_msg.twist.covariance = [0.1, 0.,  0., 0., 0., 0.,
                                               0.,  0.1, 0., 0., 0., 0.,
                                               0.,  0.,  0., 0., 0., 0.,
                                               0.,  0.,  0., 0., 0., 0.,
                                               0.,  0.,  0., 0., 0., 0.,
                                               0.,  0.,  0., 0., 0., 0.1,]
        odom_estimated_msg.pose.pose.position.x = self.position_est[0]
        odom_estimated_msg.pose.pose.position.y = self.position_est[1]
        odom_estimated_msg.pose.pose.orientation = self.orientation_est
        odom_estimated_msg.pose.covariance = [0.1, 0.,  0., 0., 0., 0.,
                                              0.,  0.1, 0., 0., 0., 0.,
                                              0.,  0.,  0., 0., 0., 0.,
                                              0.,  0.,  0., 0., 0., 0.,
                                              0.,  0.,  0., 0., 0., 0.,
                                              0.,  0.,  0., 0., 0., 0.1,]
        # Publish the pose
        self.pub_robot_odom_estimated.publish(odom_estimated_msg)
        
        
    # =============================================================================
    # # Callback function for "dead-reckoning" (alternatively called "odometry")
    # =============================================================================
    def wheel_odom(self, msg_in): 
        # read displacements from message
        d_left = msg_in.disp0
        d_right = msg_in.disp1
        
        # Compute the CHANGE in displacement of each wheel
        # Old values are in self.d_left_previous and self.d_right_previous.
        diff_left = d_left - self.d_left_previous
        diff_right = d_right - self.d_right_previous
        
        # STORE the new values of d_left and d_right for the next call
        self.d_left_previous = d_left
        self.d_right_previous = d_right
        
        # compute change in path length and change in angle
        # use "diff_left" and "diff_right" which were set a few lines above. 
        diff_pathlength = (diff_left + diff_right)/2
        diff_theta = (diff_right - diff_left)/self.wheel_width
        time_curr = self.get_clock().now().nanoseconds
        diff_time = (time_curr - self.time_prev)/1e9

        self.speed = diff_pathlength/diff_time
        self.spin_rate = diff_theta/diff_time

        self.time_prev = time_curr

        # average theta during the last time period is the midway point between old theta and new theta
        theta_avg = self.theta_est + diff_theta/2

        self.position_est[0] -= np.sin(theta_avg)*diff_pathlength
        self.position_est[1] += np.cos(theta_avg)*diff_pathlength

        self.theta_est += diff_theta # update estimate of theta to match new position
        self.orientation_est = Quaternion(
            w = np.cos(self.theta_est/2),
            x=0.,
            y=0.,
            z=np.sin(self.theta_est/2))
    
def main(args=None): 
    try: 
        rclpy.init(args=args)
        wheel_odometry_instance = WheelOdom()
        rclpy.spin(wheel_odometry_instance)
    
    except: 
        traceback.print_exc()
    
    
if __name__ == '__main__':
    main()
