import sys
sys.path.append('../')
from classes import TodoTask


def robotMoveDone(**kwargs):
    bot = kwargs.get('bot')
    bot.stop()

def robotMoveTask(params, **kwargs):
    bot = kwargs.get('bot')
    val1 = params[0]
    val2 = params[1]

    dist = int(val1 + val2,16) / 100   

    bot.move_forward(dist)

def robotMoveStop(**kwargs):
    bot = kwargs.get('bot')
    bot.stop()

robotmoveForwardTask = TodoTask(
    robotMoveDone,
    robotMoveTask,
    robotMoveStop,
    name='MoveForward', 
)