#! /usr/bin/env python3

import rospy
from basics_ros.msg import weather
import random

rospy.init_node('weather_pub_node',anonymous=True)
pub=rospy.Publisher('weather_topic',weather,queue_size=10)
rate=rospy.Rate(2)
w=weather()

while not rospy.is_shutdown():
    w.location='Dhaka'
    w.temparature=random.randrange(15,40)
    w.humidity=random.randrange(30,70)
    w.pressure=85.3
    pub.publish(w)
    print(f'Location:{w.location}\nTeamparature: {w.temparature}, Humidity: {w.humidity}, Pressure: {w.pressure}')
    rate.sleep()
