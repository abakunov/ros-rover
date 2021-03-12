import rospy
import config
import time

from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

from classes import Point,Position,QuantPos

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

        self.position = Position(QuantPos(), -1 , -1)

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

        startPoint = Point(self.position.x , self.position.y)

        print("Moving from:\n",startPoint)

        loop_rate = rospy.Rate(config.DEFAULT_LOOP_RATE)
        
        msg = Twist()
        msg.linear.x = velocity

        while self.position - startPoint <= metres * config.MISTAKE_COEF:
            self.velPub.publish(msg)
            loop_rate.sleep()

        self.stop()
        print("Moved to:\n",self.position)

    def rotate(self,degrees : float) -> None:
        
        startPos = deepcopy(self.position.theta)

        msg = Twist()
        msg.angular.z = 0.1
        loop_rate = rospy.Rate(config.DEFAULT_LOOP_RATE)
        while abs(self.position.theta.toTheta() - startPos.toTheta()) < degrees:

            self.velPub.publish(msg)
            loop_rate.sleep()
        
        self.stop()

        
