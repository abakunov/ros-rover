import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from math import sqrt
from copy import deepcopy

def genCallBack() -> None: 
    vel_msg = Twist()

    vel_msg.linear.x = 0.00000000001

    moved = 0.0

    loop_rate = rospy.Rate(1)
    cmd_vel_topic = 'cmd_vel'

    velocity_pub = rospy.Publisher(cmd_vel_topic, Twist, queue_size = 0)
    velocity_pub.publish(vel_msg)
    i = 0
    while i<1:
        velocity_pub.publish(vel_msg)
        rate.sleep() 

        i+=1
    vel_msg.linear.x = 0
    velocity_pub.publish(vel_msg)


class Position():
    
    def __init__(self, x : int , y : int) :
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return "Position: x = "+str(self.x)+"; y = "+str(self.y)
    
    def __sub__(self, other) :
        return sqrt(
            (self.x - other.x) ** 2 + (self.y - other.y) ** 2
        )
        

#глобальная переменная, определяющая текущее положение робота
robot_position = Position(0 , 0)


def odometry_callback( data : Odometry ) -> None:
    robot_position.x = data.pose.pose.position.x
    robot_position.y = data.pose.pose.position.y

rospy.init_node('splus_bot', anonymous=True)

s = rospy.Subscriber("/odom", Odometry, odometry_callback)

def move_to_point():
    start_position = deepcopy(robot_position)

    print(start_position)
    

    pub = rospy.Publisher('cmd_vel' , Twist, queue_size = 1)
    msg = Twist()
    msg.linear.x = 0.1
    pub.publish(msg)

    loop_rate = rospy.Rate(1000)


    while robot_position - start_position < 0.42:
        pub.publish(msg)
        loop_rate.sleep()
    print(robot_position)
    print(robot_position - start_position)
    msg.linear.x = 0.0
    pub.publish(msg)

rate = rospy.Rate(10)
genCallBack()
move_to_point()