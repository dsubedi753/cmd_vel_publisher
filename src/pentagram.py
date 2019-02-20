#! /usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Twist
rospy.init_node('Pentagram')
print("Pentagram Trajectory")

def rotate(r):
    t0 = rospy.Time.now().to_sec()
    t = 0
    mover.angular.z = -0.5
    r = float(r)/180 * math.pi
    while 0.5* t < r:
        pub.publish(mover)
        t1 = rospy.Time.now().to_sec()
        t = t1-t0
        print("Angle",t, r*t)
        rate.sleep()
    mover.angular.z = 0
    pub.publish(mover)

def mov_loc(v):
    v = float(v)/5
    t0 = rospy.Time.now().to_sec()
    t = 0
    mover.linear.x = v
    while v*t < 2:
        pub.publish(mover)
        t1 = rospy.Time.now().to_sec()
        t = t1-t0
        print("Dist:",t,v*t)
        rate.sleep()
    mover.linear.x = 0
    pub.publish(mover)

pub = rospy.Publisher('/cmd_vel', Twist, queue_size=6)
rate = rospy.Rate(10)
mover = Twist()

while True:
  t0 = rospy.Time.now().to_sec()
  if t0 != 0: #initial time
    break

rotate(63)
mov_loc(1)
rotate(144)
mov_loc(2)
rotate(144)
mov_loc(3)
rotate(144)
mov_loc(4)
rotate(144)
mov_loc(5)


while not rospy.is_shutdown():
  
  #pub.publish(mover)
  rate.sleep()