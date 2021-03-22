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
while False:
    print(bot.calculate_ang_vel(bot.position, Point(0,5)))
    time.sleep(1)

#bot.move2point(Point(2,3))


#bot.calculate_angle(bot.position,Point(1,1))


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

def draw_req_1():
    constant = 1.2
    bot.resetOdom()
    bot.move2point(Point(1.5 * constant, 1.5 * constant))

    bot.dropTheFlag()
    sleep(10)
    bot.move2point(Point(1.5 * constant , -1.5 * constant))
    bot.dropTheFlag()
    sleep(10)
    bot.move2point(Point(-1.5 * constant , -1.5 * constant))
    bot.dropTheFlag()
    sleep(10)
    bot.move2point(Point(-1.5 * constant , 1.5 * constant))
    bot.dropTheFlag()
    sleep(10)
    bot.move_forward(2, velocity = -0.3)

def draw_req_2():
    constant = 1.2
    bot.resetOdom()
    bot.move2point(Point(0 * constant, 3 * constant))
    bot.rotate2angle(0)
    bot.dropTheFlag()
    sleep(10)
    bot.move2point(Point(0,0))
    bot.rotate2angle(90)
    bot.resetOdom()
    bot.move2point(Point(0 * constant, 3 * constant))
    bot.rotate2angle(0)
    bot.dropTheFlag()
    sleep(10)
    bot.move2point(Point(0,0))
    bot.rotate2angle(90)
    bot.resetOdom()
    bot.move2point(Point(0 * constant, 3 * constant))
    bot.rotate2angle(0)
    bot.dropTheFlag()
    sleep(10)
    bot.move2point(Point(0,0))
    bot.rotate2angle(90)
    

def draw_req_no_m2p():
    constant = 1.2
    bot.resetOdom()
    bot.move_forward(3 * constant)
    bot.dropTheFlag()
    sleep(10)
    bot.move_forward(3 * constant, velocity = -0.3)
    bot.rotate2angle(90)
    bot.resetOdom()
    bot.move_forward(3 * constant)
    bot.dropTheFlag()
    sleep(10)
    bot.move_forward(3 * constant, velocity = -0.3)
    bot.rotate2angle(90)
    bot.resetOdom()
    bot.move_forward(3 * constant)
    bot.dropTheFlag()
    sleep(10)
    bot.move_forward(3 * constant, velocity = -0.3)
    bot.rotate2angle(90)


#move2point(start,goto)

#draw_req_1()

bot.move2point(Point(1.5,1.5))