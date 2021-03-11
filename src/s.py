import rospy
from geometry_msgs.msg import Twist


rospy.init_node('splus_bot', anonymous=True)

pub = rospy.Publisher('cmd_vel' , Twist, queue_size = 10)
msg = Twist()
msg.linear.x = 0.0
pub.publish(msg)




while not rospy.is_shutdown():
    pub.publish(msg)