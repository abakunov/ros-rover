import rospy
import config
import time
import numpy as np
from math import atan2
import math

from sensor_msgs.msg import CompressedImage
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from geometryHelpers import getDeg
from classes import Point,Position,QuantPos, ServoController, LedController

from copy import deepcopy
 
class SPlusBot:

    position : Position

    #обновление координат робота
    def positionCallback(self,data : Odometry) -> None:


        

        self.position.y = +data.pose.pose.position.x
        self.position.x = -data.pose.pose.position.y
        self.position.theta.z = data.pose.pose.orientation.z
        self.position.theta.x = data.pose.pose.orientation.x
        self.position.theta.y = data.pose.pose.orientation.y
        self.position.theta.w = data.pose.pose.orientation.w
        #test print
        #print(quaternion_to_euler(data.pose.orientation))
        #print(self.position.theta.toTheta())

    def _getCurrentLocation(self) -> None:

        loop_rate = rospy.Rate(config.DEFAULT_LOOP_RATE)
        while self.position == Position(QuantPos() , -1 , -1):
            loop_rate.sleep()
            
        return

    def camera_callback(self,data):
        self.camera_data = data.data
    def __init__(self):
        
        rospy.init_node(config.INIT_NODE_NAME)

        self.odomSub = rospy.Subscriber(config.ODOM_TOPIC_NAME, Odometry, self.positionCallback)
        
        self.velPub = rospy.Publisher(config.CMD_VEL_TOPIC_NAME, Twist, queue_size = 10)
        
        self.servo = ServoController()

        self.led = LedController()
        
        self.position = Position(QuantPos(), -1 , -1)
        
        self.LINEAR_SPEED = config.DEFAULT_SPEED
        
        self.ANGULAR_SPEED = config.DEFAULT_ANGULAR_SPEED

        self.predPosition = Position(QuantPos(), -1 , -1)
        
        self.camera_subcriber = rospy.Subscriber('/front_camera/compressed' , CompressedImage, self.camera_callback)

        self.camera_data = []

        self._getCurrentLocation()

        #TODO create field for robot angular
    
    def stop(self):

        stopMessage = Twist()
        stopMessage.linear.x = 0
        stopMessage.linear.y = 0
        stopMessage.linear.z = 0

        stopMessage.angular.x = 0
        stopMessage.angular.y = 0
        stopMessage.angular.z = 0

        self.velPub.publish(stopMessage)
    
    def move_forward(self, metres : float, velocity : float = config.DEFAULT_SPEED ):

        if velocity == config.DEFAULT_SPEED:
            velocity = self.LINEAR_SPEED

        startPoint = Point(self.position.x , self.position.y)

        #print("Moving from:\n",startPoint)

        loop_rate = rospy.Rate(config.DEFAULT_LOOP_RATE)
        
        msg = Twist()
        msg.linear.x = velocity

        while self.position - startPoint <= metres * config.MISTAKE_COEF:
            self.velPub.publish(msg)
            loop_rate.sleep()

        self.stop()
        #print("Moved to:\n",self.position)

    def rotate(self,degrees : float, speed :float = -191 ) -> None:
        
        #print(degrees,"deg")
       

        if speed == -191:
            speed = self.ANGULAR_SPEED

        startPos = deepcopy(self.position.theta)

        msg = Twist()
        msg.angular.z = speed
        loop_rate = rospy.Rate(config.DEFAULT_LOOP_RATE )
        while abs(self.position.theta.toTheta() - startPos.toTheta()) < degrees:

            self.velPub.publish(msg)
            loop_rate.sleep()
        
        #time.sleep(10)
        #print("Moved from", self.position.theta.toTheta())
        #print("To: " , startPos.toTheta())

        self.stop()
    
    def rotate2angle(self, angle : float, speed : float = 0.3):
        
        print(angle,"NEED TO GO HERE")
        

        msg = Twist()
        msg.angular.z = speed
        print(speed)
        loop_rate = rospy.Rate(config.DEFAULT_LOOP_RATE )
        print(0)
        while abs(self.position.theta.toTheta() - angle )>= 1:
            abs(self.position.theta.toTheta() - angle )
            self.velPub.publish(msg)
            loop_rate.sleep()
        print(0)
        self.stop()


    def calculate_angle(self,point1, point2):
        print("selfdeg",self.position.theta.toTheta())
        print("deg:",math.degrees(atan2(point2.y - point1.y, point2.x - point1.x)))
        return math.degrees(atan2(point2.y - point1.y, point2.x - point1.x))
    
    def calculate_ang_vel(self, start, point):
        print("vel:", -0.001 *(self.calculate_angle(self.position, point) - self.position.theta.toTheta()))
        print("vel2",-0.001 * (self.calculate_angle(self.position, point) - self.position.theta.toTheta()*-1))
        if self.calculate_angle(sl)
        if self.calculate_angle(self.start, point)  < self.position.toTheta():
            return 0.1
        else:
            return -0.1

    def move2point(self, point : Point):
        
        bot_pos = self.position
        start_point = deepcopy(bot_pos)
        
        deg = getDeg((0,1) , (point.x - bot_pos.x, point.y - bot_pos.y))
        current = self.position.theta.toTheta()
        x_diff = (bot_pos.x - point.x)
        y_diff = (bot_pos.y - point.y)

        if y_diff <= 0:
            if x_diff <= 0:
                deg = deg % 360
            else:
                deg =  360 - deg
        else:
            if x_diff < 0:
                deg = deg % 360
            else:
                deg = 360 -deg


        #time.sleep(21)
        self.rotate2angle(deg)
        
        time.sleep(10)

        vel_msg = Twist()
        vel_msg.linear.x = self.LINEAR_SPEED 
        rate = rospy.Rate(config.DEFAULT_LOOP_RATE) 
        while abs(self.position - point) >= 0.1:
            vel_msg.angular.z = self.calculate_ang_vel(start_point , point)
            self.velPub.publish(vel_msg)
            rate.sleep()
        
        self.stop()


    def servoRotateHorizontal(self, angle : int):
        
        self.servo.moveHorizontal(angle)
    
    def servoRotateVertical(self, angle : int):
        self.servo.moveVertical(angle)

    def turnOnLed(self):
        self.led.turn_on()

    def dropTheFlag(self):
        self.servo.dropFlag()
    
    def turnOffLed(self):
        self.led.turn_off()
        
    