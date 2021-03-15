import sys
sys.path.append('../')
from classes import TodoTask


def RotateRightDone(**kwargs):
    bot = kwargs.get('bot')
    bot.stop()

def RotateRight(params, **kwargs):
    bot = kwargs.get('bot')
    val1 = params[0]
    val2 = params[1]
    deg = int(val1 + val2,16) 
    bot.rotate(deg, -bot.ANGULAR_SPEED)

def cancelRotateRight(**kwargs):
    bot = kwargs.get('bot')
    bot.stop()

rotateRightTask = TodoTask(
    RotateRightDone,
    RotateRight,
    cancelRotateRight,
    name='RotateRight', 
)