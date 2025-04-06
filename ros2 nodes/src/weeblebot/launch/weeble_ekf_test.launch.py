# Copyright 2018 Open Source Robotics Foundation, Inc.
# Copyright 2019 Samsung Research America
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
import launch_ros.actions
import os
import yaml
from launch.substitutions import EnvironmentVariable
import pathlib
import launch.actions
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            output='screen',
            parameters=[os.path.join(get_package_share_directory("weeblebot"), 'config', 'ekf.yaml')],
           ),
        launch_ros.actions.Node(
            package='weeblebot',
            executable='imu_mpu6050_node',
            name='imu_node',
            output='screen',
            remappings=[('imu_mpu6050', 'imu/data')],
           ),
        launch_ros.actions.Node(
            package='mobrob',
            executable='wheel_control',
            name='wheel_motor_node',
            output='screen',
            parameters=[os.path.join(get_package_share_directory("weeblebot"), 'config', 'robot_info.yaml')],
           ),
        launch_ros.actions.Node(
            package='mobrob',
            executable='encoder_odom',
            name='wheel_odometry_node',
            output='screen',
            remappings=[('wheel_odom', 'wheel/twist')],
            parameters=[os.path.join(get_package_share_directory("weeblebot"), 'config', 'robot_info.yaml')],
           ),
        launch_ros.actions.Node(
            package='weeblebot',
            executable='gamepad_input',
            name='gamepad_reader_node',
            output='screen',
           ),
        launch_ros.actions.Node(
            package='weeblebot',
            executable='gamepad_control',
            name='gamepad_processing_node',
            output='screen',
            remappings=[('motors_speed', 'wheel_speeds_desired')],
           ),
])