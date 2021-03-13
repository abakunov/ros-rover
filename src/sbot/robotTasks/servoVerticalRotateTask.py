import sys
sys.path.append('../')
from classes import TodoTask



def servoRotateVerticalDone(**kwargs):

    bot = kwargs.get('bot')

    bot.stop()

def servoRotateVertical(params, **kwargs):
    
    bot = kwargs.get('bot')

    val1 = params[0]
    val2 = params[1]

    deg = int(val1 + val2,16)  
    bot.servoRotateVertical(deg)

def servoRotateVerticalStop(**kwargs):

    bot = kwargs.get('bot')

    bot.stop()


servoRotateVerticalTask = TodoTask(
        servoRotateVerticalDone,
        servoRotateVertical,
        servoRotateVerticalStop,
        name='servoRotateVertical',
)

