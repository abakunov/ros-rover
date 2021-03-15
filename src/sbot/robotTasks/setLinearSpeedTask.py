import sys
sys.path.append('../')
from classes import TodoTask


def setLinearDone(**kwargs):
    pass

def setLinear(params, **kwargs):

    val1 = params[0]
    val2 = params[1]
    speed = int(val1 + val2,16) / 100
    bot = kwargs.get('bot')

    bot.LINEAR_SPEED = speed

def cancelLinearSet(**kwargs):
    pass

setLinearTask = TodoTask(
    setLinearDone,
    setLinear,
    cancelLinearSet,
    name='SetLinear', 
)