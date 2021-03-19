from geometryHelpers import calculate_dist, quaternion_to_theta
import math
import threading
import sys
import trace
from config import VERTICAL_SERVO_TOPIC_NAME, HORIZONTAL_SERVO_TOPIC_NAME, LED_TOPIC_NAME,DROP_TOPIC_NAME
import rospy
from std_msgs.msg import UInt16

#Ориентация в квантерионах
class QuantPos:

    x : float
    y : float
    z : float
    w : float


    def __init__(self, z : float = 0 , w : float = 0 , x : float = 0, y : float  = 0):
        self.w = w
        self.z = z
        self.x = x
        self.y = y

    def __sub__(self, other):
        return (self.toTheta() - other.toTheta())%360
    
    def toTheta(self):
        return quaternion_to_theta(self)

    def __repr__(self):
        return "quant:"+str(self.x)+str(self.y)+str(self.z)+str(self.w)+"\n deg:"+str(self.toTheta())


#Класс точки  
class Point():
    
    def __init__(self, x : float , y : float) :
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return "Point: x = "+str(self.x)+"; y = "+str(self.y)
    
    def __eq__(self, other) -> bool:

        if self.x == other.x and self.y == other.y:
            return True
        
        return False
    
    def __sub__(self, other) -> float:
        return calculate_dist(self, other)

#класс позиции робота вместе с углом поворота
class Position(Point):
    
    theta : QuantPos

    def __init__(self, theta : QuantPos, *args, **kwargs):
        self.theta = theta
        super(Position, self).__init__(*args,**kwargs)

    def __repr__(self):
        return super(Position,self).__repr__()+"\n"+self.theta.__repr__()

#поток, который можно убить
class KThread(threading.Thread):
    def __init__(self, *args, **keywords):
        threading.Thread.__init__(self, *args, **keywords)
        self.killed = False

    def start(self):
        self.__run_backup = self.run
        self.run = self.__run            
        threading.Thread.start(self)

    def __run(self):
        sys.settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup

    def globaltrace(self, frame, why, arg):
        if why == 'call':
            return self.localtrace
        else:
            return None

    def localtrace(self, frame, why, arg):
        if self.killed:
            if why == 'line':
                raise SystemExit()
        return self.localtrace

    def kill(self):
        self.killed = True

class ActiveTask:

    def __init__(self, task = None):
        self.task = task
    
    def change(self, new_value):
        self.task = new_value

    def __repr__(self):
        return self.task.__repr__()

#таск для очереди
class TodoTask():


    def __init__(self, doneCallback, task, stopFunction,*args,name = "todotask", **kwargs ):
        
        self.doneCallback = doneCallback
        self.task = task
        self.stopFunction = stopFunction
        self.done = False
        self.name = name
        self.status = "Waiting"
        self.params = args
        self.queue = None
        self.activeTask = None
        self.bot = None

    def run(self):
        self.status = "Running"
        self.thread = KThread(target = self.worker, )
        self.thread.start()

    def worker(self):
        self.task(self.params, bot = self.bot)
        self.status = "Done"
        self.queue.pop(0)
        self.activeTask.change(None)
        self.doneCallback(bot = self.bot)
        


    def pause(self):
        #TODO implement the pause
        self.thread.do_run = not self.thread.do_run
        print("Pause")

    def stop(self):
        
        self.thread.kill()
        self.status = "Killed"
        self.activeTask.change(None)
        while self.queue : self.queue.pop(0)
        self.stopFunction(bot = self.bot)

    def __repr__(self):

        return "Task. Status : {}. Name : {}".format(self.status,self.name)


class ServoController:
    

    def __init__(self):
        self.pub1 = rospy.Publisher(HORIZONTAL_SERVO_TOPIC_NAME, UInt16, queue_size=10)
        self.pub2 = rospy.Publisher(VERTICAL_SERVO_TOPIC_NAME, UInt16, queue_size=10)
        self.dropPub = rospy.Publisher(DROP_TOPIC_NAME, UInt16, queue_size = 10)
    def moveHorizontal(self,deg:int):
        self.pub1.publish(deg)
    
    def moveVertical(self,deg:int):
        
        self.pub2.publish(deg)

    def dropFlag(self):
        self.dropPub.publish(0)

class LedController:

    pub = rospy.Publisher(LED_TOPIC_NAME, UInt16, queue_size=10)

    def turn_on(self):
        self.pub.publish(1) 
    
    def turn_off(self):
        self.pub.publish(0) 