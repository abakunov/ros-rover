import rospy
import config
import time

from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

from classes import Point

from copy import deepcopy

class SPlusBot:

    #обновление координат робота
    def positionCallback(self,data : Odometry) -> None:
        self.position.x = data.pose.pose.position.x
        self.position.y = data.pose.pose.position.y

    def _getCurrentLocation(self) -> None:

        loop_rate = rospy.Rate(config.DEFAULT_LOOP_RATE)
        while self.position == Point(0 , 0):
            loop_rate.sleep()
            
        return

    def __init__(self):

        rospy.init_node(config.INIT_NODE_NAME)
        self.odomSub = rospy.Subscriber(config.ODOM_TOPIC_NAME, Odometry, self.positionCallback)
        self.velPub = rospy.Publisher(config.CMD_VEL_TOPIC_NAME, Twist, queue_size = 10)

        self.position = Point(0 , 0)

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
    
    def move_forward(self, metres : float):

        startPosition = deepcopy(self.position)

        print("Moving from:\n",startPosition)

        loop_rate = rospy.Rate(config.DEFAULT_LOOP_RATE)
        
        msg = Twist()
        msg.linear.x = config.DEFAULT_SPEED

        while self.position - startPosition <= metres * config.MISTAKE_COEF:
            self.velPub.publish(msg)
            loop_rate.sleep()

        self.stop()
        print("Moved to:\n",self.position)

    def rotate(self,degrees : float) -> None:
        pass        
