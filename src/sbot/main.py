from splusbot import SPlusBot
from time import sleep
from classes import Position,Point
import serial

bot = SPlusBot()


#print(bot.position.theta.toTheta())

#bot.move_forward(1,0.2)
bot.rotate(359,0.6)
#bot.stop() 

#sleep(2)
#print(bot.position.theta.toTheta())

sleep(2)