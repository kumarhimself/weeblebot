from setuptools import find_packages, setup

package_name = 'weeblebot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
            'gamepad_input = weeblebot.gamepad_input:main'
        ],
    },
)
