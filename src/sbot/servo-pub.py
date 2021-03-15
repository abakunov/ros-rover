import rospy
from std_msgs.msg import UInt16
from time import sleep
import random
from config import VERTICAL_SERVO_TOPIC_NAME, HORIZONTAL_SERVO_TOPIC_NAME

class ServoController:

    pub1 = rospy.Publisher(VERTICAL_SERVO_TOPIC_NAME, UInt16, queue_size=10)
    pub2 = rospy.Publisher(HORIZONTAL_SERVO_TOPIC_NAME, UInt16, queue_size=10)

    def moveHorizontal(self,deg:int):
        self.pub1.publish(deg)
    
    def moveVertical(self,deg:int):
        self.pub2.publish(deg)

def test():
    rospy.init_node('sevo_test_node')
    serv = ServoController()
    while True:
        serv.moveHorizontal(int(input()))