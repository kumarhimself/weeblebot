#!/usr/bin/env python3

import numpy as np
import rospy
import encoders
import traceback

import encoders_and_motors as encmot

# IMPORT the custom messages:
from weeble_bot_util.msg import SensorsRaw, WheelAngles, WheelDisplacements
from mobrob_util.msg import ME439WheelAngles, ME439WheelDisplacements

#==============================================================================
# # Get parameters from rosparam
#==============================================================================
counts_per_encoder_revolution = rospy.get_param('/counts_per_encoder_revolution')  # 12.0
gear_ratio = rospy.get_param('/gear_ratio') # standard ME439 robot: 120.0   
wheel_radius = rospy.get_param('/wheel_diameter_actual')/2.0 # 0.030 # meters

encoder_update_rate = rospy.get_param('/encoder_update_rate_hz')

e0_direction_sign = rospy.get_param('/left_encoder_sign')
e1_direction_sign = rospy.get_param('/right_encoder_sign')
m0_direction_sign = rospy.get_param('/left_motor_sign')
m1_direction_sign = rospy.get_param('/right_motor_sign')

# Max encoder increment (full speed) - useful for eliminating errors
enc_increment_max = 1000


def talker(): 
    # Launch a node called "encoder_reading_node"
    rospy.init_node('encoder_reading_node', anonymous=False)
        
#==============================================================================
#     # Create two Quadrature Encoder instances, one for each wheel 
#==============================================================================
    #   constructor function call: new_variable = encmot.quadrature_encoder(serial_string_identifier, counts_per_encoder_revolution, gear_ratio, wheel_radius, forward_encoder_rotation_sign)
    qe0 = encmot.quadrature_encoder("E0", counts_per_encoder_revolution,gear_ratio, wheel_radius, e0_direction_sign)
    qe1 = encmot.quadrature_encoder("E1",counts_per_encoder_revolution,gear_ratio, wheel_radius, e1_direction_sign)
   
    encoder_update([qe0,qe1])


    
def encoder_update(quad_encoders, mot_controllers=None):
    # Create the publisher for the topic "/robot_wheel_angles", with message type "WheelAngles"    
    pub_robot_wheel_angles = rospy.Publisher('/robot_wheel_angles', ME439WheelAngles, queue_size = 10)
    # Create the publisher for the topic "/robot_wheel_displacements", with message type "WheelDisplacements"    
    pub_robot_wheel_displacements = rospy.Publisher('/robot_wheel_displacements', ME439WheelDisplacements, queue_size = 10)


    #Make messages to fill later.
    robot_wheel_angles_message = ME439WheelAngles()
    robot_wheel_angles_message.ang_left = 0. 
    robot_wheel_angles_message.ang_right = 0. 

    robot_wheel_displacements_message = ME439WheelDisplacements()
    robot_wheel_displacements_message.d_left = 0.
    robot_wheel_displacements_message.d_right = 0.
    
    #Need elapsed time between loops even though it should be about 1/(encoder_update_rate)
    t0_previous = t1_previous = rospy.get_rostime()
    publishCount = 0
    rosTimer = rospy.Rate(encoder_update_rate);
    while not rospy.is_shutdown():
        #read the encoders:
        [leftEnc,rightEnc] = encoders.readEncoders();
        
        #processing for left encoder.
        t0 = rospy.get_rostime()   # or time.time()
        dt0 = (t0-t0_previous).to_sec()
        t0_previous = t0 # store it for the next round
        #update PID loops
        quad_encoders[0].update(leftEnc, dt0)
        robot_wheel_angles_message.ang_left = quad_encoders[0].radians
        robot_wheel_displacements_message.d_left = quad_encoders[0].meters
        
        #processing for right encoder.
        t1 = rospy.get_rostime()   # or time.time()
        dt1 = (t1-t1_previous).to_sec()
        t1_previous = t1 # store it for the next round
        #update PID loops
        quad_encoders[1].update(rightEnc, dt1)
        robot_wheel_angles_message.ang_right = quad_encoders[1].radians
        robot_wheel_displacements_message.d_right = quad_encoders[1].meters

        publishCount += 1
        #only publish every 10 loops to avoid overloading ROS (should be ~10Hz)
        if (publishCount % 10 == 0):
            # Publish a message to the "/robot_wheel_angles" topic
            pub_robot_wheel_angles.publish(robot_wheel_angles_message)
            # Publish a message to the "/robot_wheel_displacements" topic
            pub_robot_wheel_displacements.publish(robot_wheel_displacements_message)
 
        rosTimer.sleep()

if __name__ == '__main__':
    try: 
        talker()
    except rospy.ROSInterruptException: 
        traceback.print_exc()
        pass
