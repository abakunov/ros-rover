from classes import TodoTask

def robotMoveDone():
    global activeTask
    queue.pop(0)
    activeTask = None
    bot.stop()

def robotMoveTask(v1,v2):
    global queue,activeTask
    bot.move_forward(1,0.2)

def robotMoveStop():
    bot.stop()
    activeTask = None
    queue = []

robotMoveTask = TodoTask(
    robotMoveDone,
    robotMoveTask,
    robotMoveStop
)