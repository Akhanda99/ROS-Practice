#! /usr/bin/env python3

import rospy
from basics_ros.msg import weather

def weather_review(msg):
    if msg.temparature>30:
        print("It's very HOT outside. Wear light clothes")
    elif msg.temparature<25:
        print("It's cold Outside. Wear warm clothes")

rospy.init_node('weather_subs_node', anonymous=True)
rospy.Subscriber('weather_topic',weather, weather_review)
rospy.spin()