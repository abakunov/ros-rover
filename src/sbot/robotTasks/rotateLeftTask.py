import sys
sys.path.append('../')
from classes import TodoTask

def RotateLeftDone(**kwargs):
    bot = kwargs.get('bot')
    bot.stop()

def RotateLeft(params,**kwargs):
    bot = kwargs.get('bot')
    val1 = params[0]
    val2 = params[1]
    deg = int(val1 + val2,16) 

    bot.rotate(deg, -bot.ANGULAR_SPEED)

def cancelRotateLeft(**kwargs):
    bot = kwargs.get('bot')
    bot.stop()

rotateLeftTask = TodoTask(
    RotateLeftDone,
    RotateLeft,
    cancelRotateLeft,
    name='RotateLeft', 
)