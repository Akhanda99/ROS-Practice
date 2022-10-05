#! /usr/bin/env python3

#Still working on It

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def laser_callback(msg):
    midlaserData=msg.ranges[0]
    leftLaserData=msg.ranges[90]
    rightLaserData=msg.ranges[270]
    backLaserData=msg.ranges[180]
    print(f'Mid: {midlaserData}, Left: {leftLaserData}, Right: {rightLaserData}')

    pub=rospy.Publisher('/cmd_vel',Twist,queue_size=10)
    vel=Twist()

    if midlaserData<1:
        if leftLaserData>0.5 and rightLaserData>0.5:
            vel.angular.z=0.2
        elif leftLaserData<0.5 and rightLaserData>0.5:
            vel.linear.x=0.02
            vel.angular.z=-0.2
        elif leftLaserData>0.5 and rightLaserData<0.5:
            vel.linear.x=0.02
            vel.angular.z=0.2
        else:
            vel.linear.x=0

    else:
        # vel.linear.x=0.2
        if leftLaserData>0.1 and rightLaserData>0.1:
            vel.linear.x=0.2
        elif leftLaserData<0.1 and rightLaserData>0.1:
            vel.angular.z=-0.2
        elif leftLaserData>0.1 and rightLaserData<0.1:
            vel.angular.z=0.2
    pub.publish(vel)



rospy.init_node('Obstacle_avoiding_node', anonymous=True)
rospy.Subscriber('/scan',LaserScan, laser_callback)
rospy.spin()