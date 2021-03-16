import serial
from time import sleep
import numpy as np
import cv2

def reciving_data():
    port = "/dev/tty.usbserial-0001"
    ser = serial.Serial(port, 19200)
    recived = b'' 
    while True:
        
        received_data = ser.read()              
        sleep(0.03)
        data_left = ser.inWaiting()             
        received_data += ser.read(data_left)
        print(received_data)
        if received_data == b'-1':
            return recived
        recived += received_data
        

def show_image(data : bytes):
    data_img = np.fromstring(data,dtype=np.uint8)
    img = cv2.imdecode(data_img, 1)
    cv2.imshow('image',img)
    cv2.waitKey(0)

def main():
    res = reciving_data()
    print(res)

    show_image(res)
