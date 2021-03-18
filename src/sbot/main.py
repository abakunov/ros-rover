from splusbot import SPlusBot
from time import sleep
from classes import Position,Point
import serial
 
bot = SPlusBot()

#print("oinit")

#print(bot.position.theta.toTheta())

#bot.move_forward(0.4,0.2)
bot.move2point(Point(0.5,0.5))
#print(bot.position.theta.toTheta())
#bot.stop() 
#bot.rotate(90,0.3)
#bot.rotate2angle(180)
#bot.stop()
#bot.servoRotateHorizontal(20)
sleep(2)
#print(bot.position.theta.toTheta())

