#! /usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Twist

def sign(x):
  if (x < 0):
    return -1
  return 1

rospy.init_node('Infinity')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=6)
rate = rospy.Rate(1)
count = Twist()
count.linear.x = 1
count.linear.y = 0
count.linear.z = 0
count.angular.x = 0
count.angular.y = 0
s=1

while not rospy.is_shutdown():
  count.angular.z = s*0.5
  pub.publish(count)
  rate.sleep()