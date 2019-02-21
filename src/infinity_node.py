#! /usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Twist

rospy.init_node('Infinity')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=6)

rate = rospy.Rate(100)
mover = Twist()
mover.linear.x = 1

s=1 #Sign of angluar velocity
print("Infinity Trajectory")

while True:
  t0 = rospy.Time.now().to_sec()
  if t0 != 0: #initial time
    break

while not rospy.is_shutdown():
  t1 = rospy.Time.now().to_sec()
  t = t1-t0 #Elapsed time
  if t >= (4*math.pi): #if the elapsed time is greater than equal to Time Period of 1 circle
    s = -s
    t0 = rospy.Time.now().to_sec()
  mover.angular.z = s*0.5
  pub.publish(mover)
  rate.sleep()