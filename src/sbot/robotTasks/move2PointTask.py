import sys
sys.path.append('../')
from classes import TodoTask


def M2PDone(**kwargs):
    bot = kwargs.get('bot')
    bot.stop()

def Move2Task(params, **kwargs):
    print(params)
    print(kwargs)

    bot = kwargs.get('bot')
    m2p_x = params[0]
    m2p_y = params[1]


    bot.move2point(Point(m2p_x,m2p_y))

def Move2PointStop(**kwargs):
    bot = kwargs.get('bot')
    bot.stop()

MoveToPointTask = TodoTask(
    M2PDone,
    Move2Task,
    Move2PointStop,
    name='Move2Point', 
)