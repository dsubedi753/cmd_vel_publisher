#! /usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Twist
rospy.init_node('Pentagram')
print("Pentagram Trajectory")

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=6)
rate = rospy.Rate(1)
mover = Twist()

r = 0.8*math.pi/2
t = 0

mover.angular.z =0
mover.linear.x = 1

while not rospy.is_shutdown():
    if t == 2 and mover.angular.z == 0:
        t = 0
        mover.linear.x = 0
        mover.angular.z = r
    if t == 2 and mover.linear.x == 0:
        t = 0
        mover.angular.z = 0
        mover.linear.x = 1
    pub.publish(mover)
    t=t+1
    rate.sleep()
    