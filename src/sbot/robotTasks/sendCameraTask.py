import sys
sys.path.append('../')
from classes import TodoTask, ActiveTask,ServoController
from splusbot import SPlusBot
import serial
import rospy
import time
import config

def send_data(data):

    print(type(data))
    # time.sleep(5)
    ser = serial.Serial(config.SERIAL_PORT, 19200)

    pack_size = 1024          
    print(0)
    pack_num  = int(len(data)/pack_size)+1
    for i in range(0, pack_num):
        serial_pack = data[i*pack_size:(i+1)*pack_size]
        send_bytes = ser.write(serial_pack)
        rospy.loginfo("Send data pack%i/%i: %s", i, pack_num, send_bytes)
        time.sleep(0.5)
    print("Exiting")
    time.sleep(10)
    ser.write(b'-1')
    rospy.loginfo("The end of file upload")


def CameraTaskDone(**kwargs):
    pass


def CameraTask(params, **kwargs):
    
    bot = kwargs.get('bot')
    data = bot.camera_data
    send_data(data)

def CameraTaskStop(**kwargs):
    pass

senPictureFromCamTask = TodoTask(
        CameraTaskDone,
        CameraTask,
        CameraTaskStop,
        name='SenThePic',
)

