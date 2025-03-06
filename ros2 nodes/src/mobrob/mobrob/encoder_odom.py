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
from geometry_msgs.msg import Pose2D
from geometry_msgs.msg import TwistWithCovarianceStamped
from mobrob_interfaces.msg import ME439WheelDisplacements

    
class WheelOdom(Node): 
    def __init__(self):
        super().__init__('wheel_odom')

        # Variables for the robot's wheel displacements (to keep knowledge of it from one step to the next)
        self.d_left_previous = 0.
        self.d_right_previous = 0.
        # Rate to set how often the estimated "pose" is published
        self.f = 10.     # Hz 
        #==============================================================================
        # # Get parameters from rosparam
        # # NOTE this is the Estimator, so we should use the "model" parameters. 
        # # This will enable us to compare the "simulated" robot (considered the true robot location) 
        # #  and the "estimated" robot (position estimated based on dead-reckoning)
        #==============================================================================
        self.declare_parameters(
        namespace='',
        parameters=[
            ('wheel_width', 0.584),
            ('wheel_diameter', 0.28),
        ])
    
        self.sub_wheel_disps = self.create_subscription( ME439WheelDisplacements, '/wheel_displacements', self.wheel_odom, 1 )  
            
        self.pub_robot_twist_estimated = self.create_publisher(TwistWithCovarianceStamped, '/wheel_odom', 1)
        self.robot_twist_estimated_message = TwistWithCovarianceStamped()

        # =============================================================================
        #     # Timer to set a publication rate. This calls a publication callback
        # =============================================================================
        self.pub_timer = self.create_timer(1.0/self.f, self.pub_callback)
    
    # =============================================================================
    #     # Callback to do the publication
    #     # This function is called by the timer above at a constant rate. Its job is to publish the current estimate of the robot pose. 
    # =============================================================================
    def pub_callback(self): 
        # Pack the message
        self.robot_twist_estimated_message.header.stamp = rclpy.get_clock().now().to_msg()
        self.robot_twist_estimated_message.header.frame_id = 'base_link'
        self.robot_twist_estimated_message.twist.linear.x = 0
        self.robot_twist_estimated_message.twist.linear.y = 0
        self.robot_twist_estimated_message.twist.angular.z = 0
        self.robot_twist_estimated_message.twist.covariance = [0.1, 0,   0, 0, 0, 0,
                                                               0,   0.1, 0, 0, 0, 0,
                                                               0,   0,   0, 0, 0, 0,
                                                               0,   0,   0, 0, 0, 0,
                                                               0,   0,   0, 0, 0, 0,
                                                               0,   0,   0, 0, 0, 0.1,]
        # Publish the pose
        self.pub_robot_twist_estimated.publish(self.robot_twist_estimated_message)
        
        
    # =============================================================================
    # # Callback function for "dead-reckoning" (alternatively called "odometry")
    # =============================================================================
    def wheel_odom(self, msg_in): 
    ####    CODE HERE: extract the wheel displacements from the message in variable msg_in. 
        # REPLACE the zeros with the proper expressions. 
        # Look in the message file for ME439WheelDisplacements.msg to find the variable 
        # names for left and right wheel displacements. 
        # Or, just ask ROS: "ros2 interface show mobrob_interfaces/msg/ME439WheelDisplacements"
        # Syntax is msg_in.variable_name
        d_left = msg_in.disp0
        d_right = msg_in.disp1
        
    ####    CODE HERE: Compute the CHANGE in displacement of each wheel
        # Old values are in self.d_left_previous and self.d_right_previous.        
        # REPLACE the zeros with the proper expressions. 
        diff_left = d_left - self.d_left_previous
        diff_right = d_right - self.d_right_previous
        
    ####    CODE HERE: STORE the new values of d_left and d_right for the next call
        # REPLACE the zeros with the proper expressions. 
        self.d_left_previous = d_left
        self.d_right_previous = d_right
        
    ####    CODE HERE: compute change in path length and change in angle
        # REPLACE the zeros with the proper expressions (see lecture notes). 
        # use "diff_left" and "diff_right" which were set a few lines above. 
        diff_pathlength = (diff_left + diff_right)/2
        diff_theta = (diff_right - diff_left)/self.wheel_width

    ####    CODE HERE: compute the AVERAGE heading angle (theta) during the movement 
        # That's halfway between the old angle and the new.
        # This makes the dead-reckoning more accurate than using just the old theta or the new one. 
        theta_avg = self.theta_estimated + diff_theta/2
        
    ####    CODE HERE: compute the change in position and heading according to the dead-reckoning equations
        # REPLACE the zeros with the proper expressions (see lecture notes). 
        # Remember that sine and cosine are in the "numpy" package, which has been imported as "np"
        self.r_center_world_estimated[0] = self.r_center_world_estimated[0] + -np.sin(theta_avg)*diff_pathlength      # x-direction position
        self.r_center_world_estimated[1] = self.r_center_world_estimated[1] + np.cos(theta_avg)*diff_pathlength      # y-direction position
        self.theta_estimated = self.theta_estimated + diff_theta

    #==============================================================================
    #     End of function "dead_reckoning"
    #==============================================================================
    
    #==============================================================================
    #     # End of function "set_pose"
    #==============================================================================
    
    
    
def main(args=None): 
    try: 
        rclpy.init(args=args)
        wheel_odometry_instance = WheelOdom()
        rclpy.spin(wheel_odometry_instance)
    
    except: 
        traceback.print_exc()
    
    
if __name__ == '__main__':
    main()
