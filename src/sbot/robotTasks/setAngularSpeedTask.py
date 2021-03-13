import sys
sys.path.append('../')
from classes import TodoTask


def setAngularDone(**kwargs):
    pass

def setAngular(params,**kwargs):
    
    bot = kwargs.get('bot')
    val1 = params[0]
    val2 = params[1]
    speed = int(val1 + val2,16) / 100

    bot.ANGULAR_SPEED = speed

def cancelAngularSet(**kwargs):
    pass

setAngularTask = TodoTask(
    setAngularDone,
    setAngular,
    cancelAngularSet,
    name='SetAngular', 
)