import rospy
from std_msgs.msg import UInt16
from time import sleep
import random

rospy.init_node('main_node')

class ServoController:
    pub1 = rospy.Publisher('horizontal_servo', UInt16, queue_size=10)
    pub2 = rospy.Publisher('vertical_servo', UInt16, queue_size=10)
    def moveHorizontal(self,deg:int):
        self.pub1.publish(deg)
    def moveVertical(self,deg:int):
        self.pub2.publish(deg)

serv = ServoController()
while True:
    serv.moveHorizontal(int(input()))
