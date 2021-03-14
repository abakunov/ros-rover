from splusbot import SPlusBot
from time import sleep
from classes import Position,Point
import serial

bot = SPlusBot()

#print("oinit")

#print(bot.position.theta.toTheta())

bot.move_forward(0.4,0.2)
#bot.move2point(Point(0.5,0.5))
#bot.stop() 

#sleep(2)
#print(bot.position.theta.toTheta())

