import sys
sys.path.append('../')
from classes import TodoTask


def ledOnDone(**kwargs):
    pass

def ledOn(params, **kwargs):
    bot = kwargs.get('bot')
    bot.led.turn_on()

def cancelledOnDone(**kwargs):
    pass

ledOnTask = TodoTask(
    ledOnDone,
    ledOn,
    cancelledOnDone,
    name='LedOn', 
)

def ledOffDone(**kwargs):
    pass

def ledOff(params, **kwargs):
    bot = kwargs.get('bot')
    bot.led.turn_off()

def cancelledOffDone(**kwargs):
    pass

ledOffTask = TodoTask(
    ledOffDone,
    ledOff,
    cancelledOffDone,
    name='LedOff', 
)