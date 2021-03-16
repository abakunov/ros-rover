import sys
import serial
import config
sys.path.append('../')
from classes import TodoTask


def SendPhotoDone(**kwargs):
    pass

def SendPhoto(params, **kwargs):
    bot = kwargs.get('bot')

    data = bot.cam_data.data

    ser = serial.Serial(config.SERIAL_PORT, 19200)
    pack_size = 800 
    pack_num  = int(len(data)/pack_size)+1
    for i in range(0, pack_num):
        serial_pack = data[i*pack_size:(i+1)*pack_size]
        send_bytes = ser.write(serial_pack)
        rospy.loginfo("Send data pack%i/%i: %s", i, pack_num, send_bytes)
        time.sleep(1)
    ser.write(b'-1')
    

def cancelSendPhoto(**kwargs):
    pass

SendPhotoTask = TodoTask(
    SendPhotoDone,
    SendPhoto,
    cancelSendPhoto,
    name='SendPhotoTask', 
)