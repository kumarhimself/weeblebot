## Based on our old launch file (weeblebot_gamepad.launch), these are the nodes we used to drive the ROS1 version of the robot

|old node location|new node location|purpose|updated to ros2?|notes|
|-------|------|-------|-----|-----|
|weeble_bot_util/gamepad_input.py|weeblebot/gamepad_input.py|connect to and publish readings from the gamepad|yes|configured to work with a controller we no longer have :(|
|weeble_bot/gamepad_control.py|weeblebot/gamepad_control.py|turn gamepad inputs into motor speed commands|yes||
|weeble_bot_util/imu_mpu6050_node.py||read and publish imu data|no|working on rewriting this to work with robot-localization dead reckoning|
|motors/motor_node.py||subscribe to motor speed commands and drive gpio pins|no|should just be able to use wheel_control.py unless we want lower level control|
|mobrob/wheel_control_node.py|mobrob/wheel_control.py|talk to encoder library to publish encoder counts|yes|new node uses gpio zero encoder and motor objects instead of old kernel thing|
|mobrob/dead_reckoning.py||do dead reckoning based on published encoder readings|no|hopefully replacing with robot-localization, but still need to figure out interfacing|
|mobrob/mobile_robot_animator.py|mobrob/mobile_robot_animator.py|use matplotlib to visualize dead reckoned pose and trajectory|yes||
|weeble_bot/weeblebot_gamepad.launch||launch the nodes!|no|probably easier to fully rewrite|