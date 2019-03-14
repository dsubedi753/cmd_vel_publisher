#! /usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
import time

rospy.init_node('Pentagram')
print("Pentagram Trajectory")

mover = Twist()
mover.linear.x = 1

head = [0, -0.8*math.pi, 0.4*math.pi, -0.4*math.pi, 0.8*math.pi]
index = 0


def move():
    mover.linear.x = 1
    mover.angular.z = 0


def stop():
    mover.linear.x = 0
    mover.angular.z = 0.5


def callback(msg):
    global index, head, cor
    'Finding Euler Angle'
    q = msg.pose.pose.orientation
    orientation_list = [q.x, q.y, q.z, q.w]
    (roll, pitch, yaw) = euler_from_quaternion(orientation_list)

    if abs(yaw-head[index]) < 0.01:
        move()
        time.sleep(1)
        index = (index+1) % 5
        stop()


sub = rospy.Subscriber('/odom', Odometry, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=6)
rate = rospy.Rate(10)

while not rospy.is_shutdown():
    pub.publish(mover)
    rate.sleep()
