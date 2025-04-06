from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'weeblebot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
             ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        (os.path.join('share', package_name, 'config'), glob(os.path.join('config', '*.yaml'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ramarlow',
    maintainer_email='ramarlow@wisc.edu',
    description='nodes for weeblebot',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'test = weeblebot.test:main',
            'gamepad_input = weeblebot.gamepad_input:main',
            'imu_mpu6050_node = weeblebot.imu_mpu6050_node:main',
            'gamepad_control = weeblebot.gamepad_control:main',
        ],
    },
)
