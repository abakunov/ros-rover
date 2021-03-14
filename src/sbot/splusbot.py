import rospy
import config
import time
import numpy as np

from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

from classes import Point,Position,QuantPos, ServoController, LedController

from copy import deepcopy

class SPlusBot:

    position : Position

    #обновление координат робота
    def positionCallback(self,data : Odometry) -> None:
        self.position.x = data.pose.pose.position.x
        self.position.y = data.pose.pose.position.y
        self.position.theta.z = data.pose.pose.orientation.z
        self.position.theta.x = data.pose.pose.orientation.x
        self.position.theta.y = data.pose.pose.orientation.y
        self.position.theta.w = data.pose.pose.orientation.w
        #print(self.position.theta.toTheta())

    def _getCurrentLocation(self) -> None:

        loop_rate = rospy.Rate(config.DEFAULT_LOOP_RATE)
        while self.position == Position(QuantPos() , -1 , -1):
            loop_rate.sleep()
            
        return

    def __init__(self):
        
        rospy.init_node(config.INIT_NODE_NAME)

        self.odomSub = rospy.Subscriber(config.ODOM_TOPIC_NAME, Odometry, self.positionCallback)
        
        self.velPub = rospy.Publisher(config.CMD_VEL_TOPIC_NAME, Twist, queue_size = 10)
        
        self.servo = ServoController()

        self.led = LedController()
        
        self.position = Position(QuantPos(), -1 , -1)
        
        self.LINEAR_SPEED = config.DEFAULT_SPEED
        
        self.ANGULAR_SPEED = config.DEFAULT_ANGULAR_SPEED
        

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
    
    def move2point(self, point : Point):
        
        bot_pos = self.position
        
        hyp = self.position - point
        
        x_diff = (bot_pos.x - point.x)
        y_diff = (bot_pos.y - point.y)

        deg = abs(np.degrees(np.arctan(y_diff / x_diff)))
        
        print(deg)
        print(x_diff,y_diff)
        time.sleep(2)


        if y_diff < 0:
            if x_diff < 0:
                print(deg)
                self.rotate(deg, -self.ANGULAR_SPEED)
            else:
                print(90 + deg)
                self.rotate(90 + deg, self.ANGULAR_SPEED)
        else:
            if x_diff < 0:
                print(deg)
                self.rotate(deg, -self.ANGULAR_SPEED)
            else:
                print(deg + 90)
                self.rotate(deg + 90, -self.ANGULAR_SPEED)
        
        time.sleep(10)

        vel_msg = Twist()
        vel_msg.linear.x = self.LINEAR_SPEED
        rate = rospy.Rate(config.DEFAULT_LOOP_RATE)
        while abs(self.position - point) >= 0.05:
            print(abs(self.position - point))
            self.velPub.publish(vel_msg)
            rate.sleep()
        
        bot.stop()


    def servoRotateHorizontal(self, angle : int):
        
        self.servo.moveHorizontal(angle)
    
    def servoRotateVertical(self, angle : int):
        self.servo.moveVertical(angle)

    def turnOnLed(self):
        self.led.turn_on()
    
    def turnOffLed(self):
        self.led.turn_off()
        
