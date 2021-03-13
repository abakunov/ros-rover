import rospy 
from sensor_msgs.msg import CompressedImage
import time
from cv_bridge import CvBridge

def callback(data):
    rospy.loginfo("I heard %s",data.data)
    time.sleep(3)

rospy.init_node('camera_handler')
s = rospy.Subscriber('/front_camera/compressed' , CompressedImage, callback)
rospy.spin()