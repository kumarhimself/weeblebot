# Weeble_Bot package Description and Members
Independent Study in UW-Madison with Professor Peter Adamczyk focusing on new bipedal robotic configuration.
<br>Team Members: (Ahphabetic)</br>
&emsp;Alli Willhite</br>
&emsp;Charles Qi</br>
&emsp;Mark Xia</br>
&emsp;Vasvi Agarwal</br>
</br>
<b> Note: </br></b>
<b>1.</b> Motor M2's power wiring is reversed to make the robot move forward. Hence, <b>motors.motor2.setSpeed(<positive number>) makes the motor2 turn CW</b>, while <b>motors.motor1.setSpeed(<positive number>) makes motor1 turns CCW</b></br>
<b>2.</b> I labeled the frontside, M1 and M2 on the robot by carving on the board using a screwdriver. </br>
# Setup
Steps to do to use this repo:</br>
1. Create a catkin_ws following the ROS tutorial</br>
<s>2. Make a package called "weeble_bot" with libraries rospy and roscpp</br></s>
2. Type "rm -rf ~/catkin_ws/src" to remove the ROS created directory; We'll substitute it with our git repo.</br>
3. Type "git clone https://yhxiaxy@bitbucket.org/yhxiaxy/src.git" under directory "~/carkin_ws"</br>
<s>5. Generate ssh public key and private key pairs; upload the public key to your github settings under "SSH and GPG keys"</br></s>
<s>&emsp;For reference: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent</br></s>
<s>&emsp;Note: the file with .pub extension is the public key while the one without it is the private key.</br></s>
<s>6. Add private key to your linux machine.</br></s>
<s>&emsp;First, start ssh-agent by typing "eval $(ssh-agent)"</br></s>
<s>&emsp;Second, add priv key by typing "ssh-add ~/.ssh/"name of private key file"</br></s>
<s>7. You should be all set for version control on git and Github. Try making minor changes to this README file and push it by typing:</s></br>
4. If you want to commit something, simply make the change and type "git add ." under the folder you changed and "git commit -m [message you want to say]", and lastly "git push"; if you are asked to log in, follow the note in the NOTE section</br>
&emsp;1. "git add ." (this adds all files under this directory to keep track of)</br>
&emsp;2. git commit -m "whatever you want to say, ex: made change to control program TYPE WITH QUOTATION MARKS!"</br>
&emsp;3. "git push origin main" or simply "git push"</br>
&emsp;Note: you can check the file status by typing "git status"</br>
# ROS Learning
Steps to learn ROS (borrowed from ECE/ME 439 by Professor Peter Adamczyk):</br>
	----------------ELEMENTARY STUFF----------------</br>
	1. Understand how ROS made modular programming possible</br>
	2. Understand ROS nodes, topics, and messages</br>
	3. Understand ROS publisher and subscriber</br>
	----------------INTERMEDIATE STUFF--------------</br>
	4. rosbag, rospaunch, rosparam, rqt_graph, rqt_plot, topic remapping</br>
	5. custom messages, ROS networking, using sensors to control motors
# ROS Tutorial. Be sure to check all topics
Reference links:</br>
	ROS node tutorial:</br>
	http://wiki.ros.org/ROS/Tutorials/UnderstandingNodes</br>
	Configure your git push authorization:</br>
	https://itsmycode.com/solved-remote-bitbucket-cloud-recently-stopped-supporting-account-passwords-for-git-authentication/</br>
	USE THE STEP 2 EXISTING REPO AND CHANGE THE COMMAND TO:</br>
	git remote set-url origin https://<Bitbucket_Username>:<App_Password>bitbucket.org/yhxiaxy/src.git</br>
	
NOTE: PLEASE CHANGE THE FIRST LINE OF talker.py AND listener.py to #!/usr/bin/env python3 INSTEAD OF #!/usr/bin/env python</br>
This is because we will use python3 to develop the robot in the future and ROS Noetic uses python3 by default</br>
