import sys
sys.path.append('../')
from classes import TodoTask, ActiveTask,ServoController
from splusbot import SPlusBot



def servoRotateHorizontalDone(**kwargs):

    bot = kwargs.get('bot')

    bot.stop()

def servoRotateHorizontal(params, **kwargs):
    
    bot = kwargs.get('bot')

    val1 = params[0]
    val2 = params[1]

    deg = int(val1 + val2,16)  
    bot.servoRotateHorizontal(deg)

def servoRotateHorizontalStop(**kwargs):

    bot = kwargs.get('bot')

    bot.stop()


servoRotateHorizontalTask = TodoTask(
        servoRotateHorizontalDone,
        servoRotateHorizontal,
        servoRotateHorizontalStop,
        name='servoRotateHorizontal',
)

