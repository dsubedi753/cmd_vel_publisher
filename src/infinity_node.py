#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

rospy.init_node('Infinity')
print("Infinity Trajectory")

mover = Twist()
mover.linear.x = 1
mover.angular.z = 0.5
phase = 0


def callback(msg):
    a = 0.1
    pub.publish(mover)
    x_val = msg.pose.pose.position.x
    y_val = msg.pose.pose.position.y
    global phase
    if x_val > 1 and y_val > 1:
        phase = 1
    if x_val > 1 and y_val < -1:
        phase = 0
    if phase == 1 and abs(x_val) < a and abs(y_val) < a:
        print("Round 2")
        mover.angular.z = -0.5
    if phase == 0 and abs(x_val) < a and abs(y_val) < a:
        print("Round 1")
        mover.angular.z = 0.5


sub = rospy.Subscriber('/odom', Odometry, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=6)
rospy.spin()
