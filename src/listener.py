import rospy
from std_msgs.msg import String
from rosgraph_msgs.msg import Log
from nav_msgs.msg import Odometry
import time


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)
    


rospy.init_node('listener', anonymous=True)
s = rospy.Subscriber("/odom", Odometry, callback)
rospy.spin()