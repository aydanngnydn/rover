#! /usr/bin/env python
import rospy
from std_msgs.msg import String


pub_1 = rospy.Publisher('/position/robotic_arm', String, queue_size=10)
pub_2 = rospy.Publisher('/position/drive', String, queue_size=10)


def sign(sayi):

      if sayi == '0':
            return int(1)

      elif sayi == '1':
            return int(-1)

 
def callback1(data): #arm 24
      veri = data.data #string tipinde data'yı atama
      #işaret belirleme
      arm1 = sign(veri[1]) * int(veri[2:5])
      arm2 = sign(veri[5]) * int(veri[6:9])
      arm3 = sign(veri[9]) * int(veri[10:13])
      arm4 = sign(veri[13]) * int(veri[14:17])
      arm5 = sign(veri[17]) * int(veri[18:21])
      arm6 = sign(veri[21]) * int(veri[22:25])

      if arm1 < -255:
            arm1 = -255
      if arm1 > 255:
            arm1 = 255

      if arm2 < -255:
            arm2 = -255
      if arm2 > 255:
            arm2 = 255

      if arm3 < -255:
            arm3 = -255
      if arm3 > 255:
            arm3 = 255

      if arm4 < -255:
            arm4 = -255
      if arm4 > 255:
            arm4 = 255

      if arm5 < -255:
            arm5 = -255
      if arm4 > 255:
            arm5 = 255

      if arm6 < -255:
            arm6 = -255
      if arm6 > 255:
            arm6 = 255

      pub_1.publish("A" + " " + str(arm1) + " " + str(arm2) + " " + str(arm3) + " " + str(arm4) + " " + str(arm5) + " " + str(arm6) + " " + "B")


def callback2(data):#drive 16
      veri = data.data

      drive1 = sign(veri[1]) * int(veri[2:5])
      drive2 = sign(veri[5]) * int(veri[6:9])
      drive3 = sign(veri[9]) * int(veri[10:13])
      drive4 = sign(veri[13]) * int(veri[14:17])

      if drive1 < -255:
            drive1 = -255
      if drive1 > 255:
            drive1 = 255

      if drive2 < -255:
            drive2 = -255
      if drive2 > 255:
            drive2 = 255

      if drive3 < -255:
            drive3 = -255
      if drive3 > 255:
            drive3 = 255

      if drive4 < -255:
            drive4 = -255
      if drive4 > 255:
            drive4 = 255

      pub_2.publish("A" + " " + str(drive1) + " " + str(drive2) + " " + str(drive3) + " " + str(drive4) + " " + "B")


def start():
	
      rospy.init_node("rover_node")

      rospy.Subscriber('/serial/robotic_arm', String, callback1)
      rospy.Subscriber('/serial/drive', String, callback2)

      rospy.spin()

if __name__ == '__main__':
      start()
