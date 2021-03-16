import rospy 
from sensor_msgs.msg import CompressedImage
import time
from cv_bridge import CvBridge

def camera_callback(data):
    rospy.loginfo("I heard %s", data.data)
    print(type(data.data))
    time.sleep(1000)

rospy.init_node('camera_handler')
s = rospy.Subscriber('/front_camera/compressed', CompressedImage, camera_callback)
rospy.spin()

# pack_size = 1024           
# pack_num  = int(len(ret_data)/pack_size)+1
# for i in range(0, pack_num):
#     serial_pack = ret_data[i*pack_size:(i+1)*pack_size]
#     send_bytes = ser.write(serial_pack)
#     rospy.loginfo("Send data pack%i: %s", i, send_bytes)
#     time.sleep(0.5)