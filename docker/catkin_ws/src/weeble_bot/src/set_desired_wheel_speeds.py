#!/usr/bin/env python3

import rospy
import traceback
import numpy as np
# Importing custom message from ROS package
from weeble_bot_util.msg import WheelSpeeds

# This python file creates a node "set_desired_wheel_speeds" and talker that publishes
# the wheel speeds to topic "wheel_speeds_desired" with message type wheelspeeds


# Use a new structure: 
# structure: 
# np.array([[duration, left_wheel_speed, right_wheel_speed], [duration, left_wheel_speed, right_wheel_speed], ...]
# 
# Example: Move Forward and Back, 2s each, 0.3 meters per second: 
stage_settings = np.array( [ [0.0, 0.0, 0.0], [5.0,0.3, 0.3], [5.0, -0.3, -0.3], [2.0, 0.0, 0.0]] )
# Example: forward, turn, return to home, turn. 
# stage_settings = np.array( [ [0,0,0],[3,0.100,0.100],[1,0,0],[1.5,0.1592,-0.1592],[1,0,0],[3,0.100,0.100],[1,0,0],[1.5,-0.1592,0.1592],[1,0,0]] )

# Convert it into a numpy array
stage_settings_array = np.array(stage_settings)
# Convert the first column to a series of times (elapsed from the beginning) at which to switch settings. 
stage_settings_array[:,0] = np.cumsum(stage_settings_array[:,0],0)  # cumsum = "cumulative sum". The last Zero indicates that it should be summed along the first dimension (down a column). 

def talker():
	# Creating a node
	rospy.init_node("set_desired_wheel_speeds", anonymous=False)
	
	# Creating a publisher with message type "wheelspeeds"
	pub_speeds = rospy.Publisher('/wheel_speeds_desired', WheelSpeeds, queue_size=10)
	
	# Initialize wheelspeeds message by giving 0 to both wheel speeds
	msg_out = WheelSpeeds()
	msg_out.speed_left = 0
	msg_out.speed_right = 0
	
	# Set up ros message publish rate
	r = rospy.Rate(100) #100hz
	
	# keep publishing the speeds while rospy is active
	while not rospy.is_shutdown():
		future_stages = np.argwhere( stage_settings_array[:,0] >= (rospy.get_rostime()-t_start).to_sec() ) 
		if len(future_stages)>0:
			stage = future_stages[0]
			print(stage)
		else: 
			break
		msg_out.speed_left = stage_settings_array[stage,1]
		msg_out.speed_right = stage_settings_array[stage,2]
		# Publish the message
		pub_speeds.publish(msg_out)
		# Log the info (optional)
#            rospy.loginfo(pub_speeds)    
		
		r.sleep()

    except Exception:
        traceback.print_exc()
        # When Errored, Zero the speeds
        msg_out.speed_left = 0
        msg_out.speed_right = 0
        pub_speeds.publish(msg_out)
        rospy.loginfo(pub_speeds)    
        pass
        
        
    # When done, Zero the speeds
    msg_out.speed_left = 0
    msg_out.speed_right = 0
    pub_speeds.publish(msg_out)
    rospy.loginfo(pub_speeds)    


# Run the talker while in main function
if __name__ == '__main__':
    try: 
        talker()
    except rospy.ROSInterruptException: 
        pass
