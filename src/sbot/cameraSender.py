import rospy 
from sensor_msgs.msg import CompressedImage
import time
import cv2
import numpy as np
from cv_bridge import CvBridge
import config
import serial
import struct


def send_data(data):

    print(type(data))
    ser = serial.Serial(config.SERIAL_PORT, 19200)

    pack_size = 1024          
    print(0)
    pack_num  = int(len(data)/pack_size)+1
    for i in range(0, pack_num):
        serial_pack = data[i*pack_size:(i+1)*pack_size]
        send_bytes = ser.write(serial_pack)
        rospy.loginfo("Send data pack%i/%i: %s", i, pack_num, send_bytes)
        time.sleep(1)
    print("Exiting")
    time.sleep(10)
    ser.write(b'-1')
    rospy.loginfo("The end of file upload")

def cbd(data):
    pass

def callback(data):
    send_data(data.data)
    exit(0)
    time.sleep(1000)

rospy.init_node('camera_handler')
s = rospy.Subscriber('/front_camera/compressed' , CompressedImage, callback)
rospy.spin()

