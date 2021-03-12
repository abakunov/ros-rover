from time import sleep
import struct
import serial
from time import sleep
import config
from classes import TodoTask
import threading
from robotTasks import *
from splusbot import SPlusBot


queue = []
activeTask = None
commands = {'64' : robotMoveTask}
bot = SPlusBot()



def parse_packages(*args):
    global queue,activeTask
    for msg in args:
        
        command, v1, v2 = struct.unpack('!3c',msg)

        command = command.hex()
        v1 = v1.hex()
        v2 = v2.hex()

        if command == config.STOP_COMMAND_NAME:
            activeTask.stop()
            continue
        if command == config.PAUSE_COMMAND_NAME:
            activeTask.pause()
            continue
        

        if command in commands:
            queue.append((commands[command]))

ser = serial.Serial(config.SERIAL_PORT, 19200)    #Open port with baud rate


def stop():
    #TODO stop the robot
    print("Stopping")
    queue = []

def move(v1,v2):
    print("Moving")



def send_bytes():
    msg = struct.pack('!3c', b'm', b'3', b'2')
    parse_packages(msg,msg,msg)


        




def set_q():
    global queue
    queue = []

def worker():

    global queue,activeTask

    while True:
        if not queue:
            sleep(0.05)
            continue
        
        if activeTask:
            
            sleep(0.05)
            continue

        activeTask = queue[0]
        activeTask.run()

        sleep(0.05)

def reciving_data():
    global queue,activeTask
    while True:
        
        received_data = ser.read()              #read serial port
        sleep(0.03)
        data_left = ser.inWaiting()             #check for remaining byte
        received_data += ser.read(data_left)
        parse_packages(received_data)
        print(queue)
        ser.write(b'Got it\n')


def main():
    workerThread = threading.Thread(target = worker)
    listenerThread = threading.Thread(target = reciving_data)
    workerThread.start()
    listenerThread.start()

main()
#unpacking multiply packages example:
#parse_packages(package1, package2, ..., package n)

#Таск вызывается
#Таск работает в отдельном треде
#Таск помечается активным
#При остановке таска производится стоп функция таска, тред убивается