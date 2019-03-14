#! /usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

rospy.init_node('ODOPUB')
rate = rospy.Rate(1)


def callbeck(msg):
    x_val = msg.pose.pose.position.x
    y_val = msg.pose.pose.position.y
    global roll, pitch, yaw
    q = msg.pose.pose.orientation
    orientation_list = [q.x, q.y, q.z, q.w]
    (roll, pitch, yaw) = euler_from_quaternion(orientation_list)
    print(x_val, y_val, yaw)


sub = rospy.Subscriber('/odom', Odometry, callbeck)
rospy.spin()
