import sys
sys.path.append('../')
from classes import TodoTask, ActiveTask,ServoController
from splusbot import SPlusBot
import time


def dropFlagDone(**kwargs):

    print("dropped")


def dropFlag(params, **kwargs):
    
    bot = kwargs.get('bot')
    bot.dropTheFlag()
    time.sleep(10)

def dropFlagStop(**kwargs):
    pass

dropTheFlagTask = TodoTask(
        dropFlagDone,
        dropFlag,
        dropFlagStop,
        name='Drop The Flag',
)

