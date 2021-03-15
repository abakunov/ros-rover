import rospy 
from sensor_msgs.msg import CompressedImage
import time
from cv_bridge import CvBridge
from std_msgs.msg import UInt16


class LedController:

    pub = rospy.Publisher('led_controller', UInt16, queue_size=10)

    def turn_on(self):
        self.pub.publish(1) 
    
    def turn_off(self):
        self.pub.publish(0)

rospy.init_node('led_controller_node')
led = LedController()

while True:
    led.turn_on()
    time.sleep(3)
    led.turn_off()
    time.sleep(3)



