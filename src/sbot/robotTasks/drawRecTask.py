import sys

sys.path.append('../')
from classes import TodoTask,Point
from splusbot import SPlusBot
import time
from time import sleep


def drawRectDone(**kwargs):

    bot = kwargs.get('bot')
    bot.stop()


def drawRect(params, **kwargs):
    
    bot = kwargs.get('bot')
    constant = 1
    bot.resetOdom()
    bot.move2point(Point(1.5 * constant, 1.5 * constant))

    bot.dropTheFlag()
    sleep(10)
    bot.move_forward(0.5)
    bot.move2point(Point(1.5 * constant , -1.5 * constant))
    bot.dropTheFlag()
    sleep(10)
    bot.move_forward(0.5)
    bot.move2point(Point(-1.5 * constant , -1.5 * constant))
    bot.dropTheFlag()
    sleep(10)
    bot.move_forward(0.5)
    bot.move2point(Point(-1.5 * constant , 1.5 * constant))
    bot.dropTheFlag()
    sleep(10)
    bot.move_forward(2, velocity = -0.3)

def drawRectStop(**kwargs):
    bot = kwargs.get('bot')
    bot.stop()

drawRectTask = TodoTask(
        drawRectDone,
        drawRect,
        drawRectStop,
        name='Draw The Rect',
)

