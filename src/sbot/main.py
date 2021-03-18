from splusbot import SPlusBot
from time import sleep
from classes import Position,Point
import serial
import numpy as np
 
#bot = SPlusBot()

#print("oinit")

#print(bot.position.theta.toTheta())

#bot.move_forward(0.4,0.2)
#bot.move2point(Point(1,1))
#print(bot.position.theta.toTheta())
#bot.stop() 
#bot.rotate(349,0.3)
#bot.rotate2angle(0)
#bot.servoRotateHorizontal(20)
#sleep(2)
#print(bot.position.theta.toTheta())

def move2point(p1:Point, point : Point):
        
    bot_pos = p1
        
    hyp = p1 - point
        
    x_diff = (bot_pos.x - point.x)
    y_diff = (bot_pos.y - point.y)
    

    deg = abs(np.degrees(np.arctan(y_diff / x_diff)))
    print(x_diff, y_diff)
    print(deg)

move2point(Point(0,0), Point(-1,1))