import sys
sys.path.append('../')
from classes import TodoTask, ActiveTask,ServoController
from splusbot import SPlusBot



def dropFlagDone(**kwargs):

    print("dropped")

    bot = kwargs.get('bot')

    bot.stop()

def dropFlag(params, **kwargs):
    
    bot = kwargs.get('bot')
    bot.dropTheFlag()

def dropFlagStop(**kwargs):
    pass

dropFlagTask = TodoTask(
        dropFlagDone,
        dropFlag,
        dropFlagStop,
        name='Drop The Flag',
)

