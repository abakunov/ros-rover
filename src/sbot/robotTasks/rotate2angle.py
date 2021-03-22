import sys
sys.path.append('../')
from classes import TodoTask

def Rotate2Done(**kwargs):
    bot = kwargs.get('bot')
    bot.stop()

def Rotate2(params,**kwargs):
    bot = kwargs.get('bot')
    val1 = params[0]
    val2 = params[1]
    deg = int(val1 + val2,16) 

    bot.nicerotate2angle(deg) 

def cancelRotate2(**kwargs):
    bot = kwargs.get('bot')
    bot.stop()

Rotate2Task = TodoTask(
    Rotate2Done,
    Rotate2,
    cancelRotate2,
    name='Rotate 2 angle', 
)