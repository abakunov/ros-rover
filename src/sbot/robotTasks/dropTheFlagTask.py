import sys
sys.path.append('../')
from classes import TodoTask, ActiveTask,ServoController
from splusbot import SPlusBot



def dropFlagDone(**kwargs):

    print("dropped")


def dropFlag(params, **kwargs):
    
    bot = kwargs.get('bot')
    bot.dropTheFlag()

def dropFlagStop(**kwargs):
    pass

pauseTask = TodoTask(
        dropFlagDone,
        dropFlag,
        dropFlagStop,
        name='Drop The Flag',
)

