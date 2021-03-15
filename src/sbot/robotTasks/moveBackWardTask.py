import sys
sys.path.append('../')
from classes import TodoTask


def robotMoveBackwardDone(**kwargs):

    bot = kwargs.get('bot')
    bot.stop()

def robotMoveBackwardTask(params, **kwargs):
    
    
    bot = kwargs.get('bot')

    val1 = params[0]
    val2 = params[1]

    dist = int(val1 + val2,16) / 100   
    bot.move_forward(dist,-bot.LINEAR_SPEED)

def robotMoveBackwardStop(**kwargs):
    
    bot = kwargs.get('bot')
    bot.stop()

robotMoveBackTask = TodoTask(
    robotMoveBackwardDone,
    robotMoveBackwardTask,
    robotMoveBackwardStop,
    name='MoveBackward', 
)