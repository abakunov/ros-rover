from time import sleep
import struct
import serial
from time import sleep
import config
from classes import TodoTask
import threading
import robotTasks
from splusbot import SPlusBot
from copy import deepcopy

##CONFVARS##

LINEAR_SPEED = 0.2
ANGULAR_SPEED = 0.2

##CONFVARS##

queue = []
activeTask = None

############COMMANDS##############

####ROBOTMOVECOMMAND##############

def robotMoveDone():
    global queue,activeTask
    queue.pop(0)
    activeTask = None
    bot.stop()

def robotMoveTask(params):
    global queue,activeTask

    print(params)
    val1 = params[0]
    val2 = params[1]

    dist = int(val1 + val2,16) / 100   
    print(LINEAR_SPEED)
    bot.move_forward(dist,LINEAR_SPEED)

def robotMoveStop():
    global queue,activeTask
    bot.stop()
    activeTask = None
    queue = []

robotMoveTask = TodoTask(
    robotMoveDone,
    robotMoveTask,
    robotMoveStop,
    name='MoveForward', 
)

####ROBOTMOVEBACKWARDCOMMAND##############

def robotMoveBackwardDone():
    global queue,activeTask
    queue.pop(0)
    activeTask = None
    bot.stop()

def robotMoveBackwardTask(params):
    global queue,activeTask

    print(params)
    val1 = params[0]
    val2 = params[1]

    dist = int(val1 + val2,16) / 100   
    print(LINEAR_SPEED)
    bot.move_forward(dist,-LINEAR_SPEED)

def robotMoveBackwardStop():
    global queue,activeTask
    bot.stop()
    activeTask = None
    queue = []

robotMoveBackTask = TodoTask(
    robotMoveBackwardDone,
    robotMoveBackwardTask,
    robotMoveBackwardStop,
    name='MoveBackward', 
)

####SETLINEARSPEED##############
def setLinearDone():

    global queue,activeTask
    queue.pop(0)
    activeTask = None

def setLinear(params):
    global LINEAR_SPEED
    val1 = params[0]
    val2 = params[1]
    speed = int(val1 + val2,16) / 100
    print("SETTING LIN", speed)
    LINEAR_SPEED = speed

def cancelLinearSet():
    global queue,activeTask
    activeTask = None
    queue = []

setLinearTask = TodoTask(
    setLinearDone,
    setLinear,
    cancelLinearSet,
    name='SetLinear', 
)

####SETLINEARSPEED##############

####SETANGULARSPEED##############
def setAngularDone():

    global queue,activeTask
    queue.pop(0)
    activeTask = None

def setAngular(params):
    global ANGULAR_SPEED
    val1 = params[0]
    val2 = params[1]
    speed = int(val1 + val2,16) / 100

    ANGULAR_SPEED = speed

def cancelAngularSet():
    global queue,activeTask
    activeTask = None
    queue = []

setAngularTask = TodoTask(
    setAngularDone,
    setAngular,
    cancelAngularSet,
    name='SetAngular', 
)

####SETANGULARSPEED##############


####ROBOTROTATELEFT##############
def RotateLeftDone():
    global queue,activeTask
    queue.pop(0)
    activeTask = None
    bot.stop()

def RotateLeft(params):
    global ANGULAR_SPEED
    val1 = params[0]
    val2 = params[1]
    deg = int(val1 + val2,16) 

    bot.rotate(deg, -ANGULAR_SPEED)

def cancelRotateLeft():
    global queue,activeTask
    activeTask = None
    queue = []
    bot.stop()

rotateLeftTask = TodoTask(
    RotateLeftDone,
    RotateLeft,
    cancelRotateLeft,
    name='RotateLeft', 
)

####ROBOTROTATELEFT##############

####ROBOTROTATERIGHT##############
def RotateRightDone():
    print("IMDONE")
    global queue,activeTask
    queue.pop(0)
    activeTask = None
    bot.stop()

def RotateRight(params):
    global ANGULAR_SPEED
    val1 = params[0]
    val2 = params[1]
    deg = int(val1 + val2,16) 
    bot.rotate(deg, ANGULAR_SPEED)

def cancelRotateRight():
    global queue,activeTask
    activeTask = None
    queue = []
    bot.stop()

rotateRightTask = TodoTask(
    RotateRightDone,
    RotateRight,
    cancelRotateRight,
    name='RotateRight', 
)

####ROBOTROTATELEFT##############


############COMMANDS##############




commands = {'64' : robotMoveTask, 'cc' : setLinearTask, 'aa' : setAngularTask, 'bb' : robotMoveBackTask,'03' : rotateLeftTask, '04' : rotateRightTask}
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
            activeTask.stop()
            continue
        if command == config.PAUSE_COMMAND_NAME:
            activeTask.pause()
            continue
        
        

        if command in commands:

            todoCommand = deepcopy(commands[command])



            todoCommand.params = [v1,v2]
            queue.append(todoCommand)

ser = serial.Serial(config.SERIAL_PORT, 19200)



def send_bytes():
    msg = struct.pack('!3c', b'm', b'3', b'2')
    parse_packages(msg,msg,msg)

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
        
        received_data = ser.read()              
        sleep(0.03)
        data_left = ser.inWaiting()             
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


