from splusbot import SPlusBot
from time import sleep
import time
import config
import rospy
from classes import Position,Point
import serial
from geometryHelpers import getDeg
import numpy as np
 
bot = SPlusBot()


#start = Point(0.,0.)
#goto = Point(-1,0.5)
#print(getDeg((0,1) , (goto.x - start.x, goto.y - start.y)))
#exit(0)
#bot.rotate2angle(0)
bot.move2point(Point(-1,0.5))
#print("bot have been inited")

#print(bot.position.theta.toTheta())

#bot.move_forward(0.4,0.2)
#bot.move2point(Point(0.5,0.5))
#sleep(5)
#bot.move2point(Point(-1,0.5))
#print(bot.position.theta.toTheta())
#bot.stop() 
#bot.rotate(349,0.3)
#bot.rotate2angle(0)
#bot.servoRotateHorizontal(20)
#sleep(2)
#print(bot.position.theta.toTheta())



#start = Point(0,0)
#goto = Point(-1,0)

def move2point(bot_pos,point):


    deg = getDeg((0,1) , (goto.x - start.x, goto.y - start.y))
    current = 0

    x_diff = (bot_pos.x - point.x)
    y_diff = (bot_pos.y - point.y)

    if y_diff <= 0:
            if x_diff <= 0:
                deg = (current + deg) % 360
            else:
                deg = (current - deg) % 360
    else:
            if x_diff < 0:
                deg = (current + deg) % 360
            else:
                deg = (current - deg) % 360
    
    print(deg)

#move2point(start,goto)

