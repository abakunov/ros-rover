from time import sleep
import struct
import serial
from time import sleep
import config
from classes import TodoTask,ServoController,ActiveTask
import threading
import robotTasks
from splusbot import SPlusBot
from copy import deepcopy
import rospy

import sys

sys.path.append('./robotTasks')
from servoVerticalRotateTask import servoRotateVerticalTask
from servoHorizontalRotateTask import servoRotateHorizontalTask
from moveForwardTask import robotmoveForwardTask
from moveBackWardTask import robotMoveBackTask
from setLinearSpeedTask import setLinearTask
from setAngularSpeedTask import setAngularTask
from rotateLeftTask import rotateLeftTask
from rotateRightTask import rotateRightTask


queue = []
activeTask = ActiveTask(None)
SERVO = ServoController()


commands = {
    '64' : robotmoveForwardTask,
    'cc' : setLinearTask,
    'aa' : setAngularTask,
    'bb' : robotMoveBackTask,
    '03' : rotateLeftTask, 
    '04' : rotateRightTask,
    '05' : servoRotateHorizontalTask,
    '06' : servoRotateVerticalTask
}


bot = SPlusBot()

def set_q():
    q = []

def parse_packages(*args):
    global queue,activeTask
    for msg in args:
        
        command, v1, v2 = struct.unpack('!3c',msg)

        command = command.hex()
        v1 = v1.hex()
        v2 = v2.hex()

        if command == config.STOP_COMMAND_NAME:
            activeTask.task.stop()
            continue
        if command == config.PAUSE_COMMAND_NAME:
            activeTask.task.pause()
            continue
        
        

        if command in commands:

            todoCommand = deepcopy(commands[command])



            todoCommand.params = [v1,v2]
            queue.append(todoCommand)


ser = serial.Serial(config.SERIAL_PORT, 19200)


def worker():
    
    global queue,activeTask
    
    while True:

        if not queue:
            sleep(0.05)
            continue
        
        if activeTask.task:
            
            sleep(0.05)
            continue

        activeTask.change(queue[0])

        activeTask.task.bot = bot
        activeTask.task.queue = queue
        activeTask.task.activeTask = activeTask

        activeTask.task.run()

        sleep(0.05)

def reciving_data():
    global queue,activeTask
    while True:
        
        received_data = ser.read()              
        sleep(0.03)
        data_left = ser.inWaiting()             
        received_data += ser.read(data_left)
        parse_packages(received_data)
        print(queue)
        #ser.write(b'Command recived \n')


def main():
    workerThread = threading.Thread(target = worker)
    listenerThread = threading.Thread(target = reciving_data)
    workerThread.start()
    listenerThread.start()

main()


