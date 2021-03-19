from flask import Flask
from flask import request
import serial
import threading
import struct
import serial.tools.list_ports
from flask_cors import CORS, cross_origin
import serial
from time import sleep
import numpy as np
import cv2
image_path = './test.png'
serial_port = ''

def reciving_data():
    print(0,"!")
    global serial_port
    port = serial_port
    ser = serial.Serial(port, 19200)
    recived = b'' 
    print("in recived")
    while True:
        print("in loop")
        received_data = ser.read()              
        sleep(0.03)
        data_left = ser.inWaiting()             
        received_data += ser.read(data_left)
        print(received_data)
        if received_data == b'-1':
            print("!!!!!!!!!!!!!!!!!11")
            data_img = np.fromstring(recived,dtype=np.uint8)
            img = cv2.imdecode(data_img, 1)
            cv2.imwrite(image_path, img) 
            return recived
        recived += received_data
        

def show_image(data : bytes):
    data_img = np.fromstring(data,dtype=np.uint8)
    img = cv2.imdecode(data_img, 1)
    cv2.imshow('image',img)
    cv2.waitKey(0)



app = Flask(__name__)
cors = CORS(app)


@app.route('/get_serial_ports/', methods=['GET'])
@cross_origin()
def get_serial_ports():
    comlist = serial.tools.list_ports.comports()
    connected = []
    for element in comlist:
        connected.append(element.device)
    response = {'ports': connected, 'status': 'OK'}
    return response

@app.route('/set_serial_port/', methods=['POST'])
@cross_origin()
def set_serial_port():
    if request.method == "POST":
        global serial_port
        data = eval(request.get_data().decode('utf-8'))
        serial_port = data['port']
        return {'status': 'OK'}
    return {'status': 'Bad Request'}

@app.route('/execute_command/', methods=['POST'])
@cross_origin()
def execute_command ():
    if request.method == "POST":
        global serial_port
        data = eval(request.get_data().decode('utf-8'))
        command = data['command']

        value = data['value']
        
        print(command)
        value = hex(int(value))[2::]

        f,s = "",""
        if len(value) == 1:
            s = "\\x0"+value
            f = "\\x00"
        elif len(value) == 2:
            s = "\\x"+value
            f = "\\x00"
        elif len(value) == 3:
            s = "\\x"+value[1::]
            f = "\\x0" + value[0]
        elif len(value) == 4:
            s = "\\x"+value[2:]
            f = "\\x"+value[:3:]
        print("COMMAND",command)
        if command == 'ba':
            command = eval("b'\\x"+command+"'")
            strcuted_data = struct.pack('!3c', command, eval("b'"+f+"'") , eval("b'"+s+"'"))
            port = serial.Serial(serial_port, 19200)
            port.setDTR(False)
            port.write(strcuted_data)
            port.cancel_write()
            recived = b''
            while True:
                print("in loop")
                received_data = port.read()              
                sleep(0.03)
                data_left = port.inWaiting()             
                received_data += port.read(data_left)
                print(received_data)
                if received_data == b'-1':
                    print("!!!!!!!!!!!!!!!!!11")
                    data_img = np.fromstring(recived,dtype=np.uint8)
                    img = cv2.imdecode(data_img, 1)
                    cv2.imwrite(image_path, img) 
                    return  {'status': 'OK'}
                recived += received_data
            return {'status': 'OK'}
        command = eval("b'\\x"+command+"'")
        strcuted_data = struct.pack('!3c', command, eval("b'"+f+"'") , eval("b'"+s+"'"))
        port = serial.Serial(serial_port, 19200)

        port.write(strcuted_data)
        return {'status': 'OK'}

    return {'status': 'Bad Request'}


def FlaskThread():
    app.run(host='0.0.0.0')



def camera_check():
    while True:
        if not serial_port:
            continue
        reciving_data()
    

if __name__ == "__main__":
    fsk = threading.Thread(target = FlaskThread)
    

    #cmr.start()
    fsk.start()