import rospy 
from sensor_msgs.msg import CompressedImage
import time
import cv2
import numpy as np
from cv_bridge import CvBridge
import zlib


def callback(data):
    rospy.loginfo(dir(data))
    #rospy.loginfo(data.deserialize_numpy)
    data_img = np.fromstring(data.data,dtype=np.uint8)
    img = cv2.imdecode(data_img, 1)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    #rospy.loginfo("I heard %s",data.data)
    time.sleep(3)

rospy.init_node('camera_handler')
s = rospy.Subscriber('/front_camera/compressed' , CompressedImage, callback)
rospy.spin()