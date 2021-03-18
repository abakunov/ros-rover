from splusbot import SPlusBot
from time import sleep
from classes import Position,Point
import serial
import numpy as np
 
bot = SPlusBot()

print("bot have been inited")

#print(bot.position.theta.toTheta())

#bot.move_forward(0.4,0.2)
bot.move2goal(Point(0.5,0.5))

#print(bot.position.theta.toTheta())
#bot.stop() 
#bot.rotate(349,0.3)
#bot.rotate2angle(0)
#bot.servoRotateHorizontal(20)
sleep(2)
#print(bot.position.theta.toTheta())

