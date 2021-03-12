from tf.transformations import quaternion_multiply, quaternion_inverse, euler_from_quaternion
from math import degrees
import rospy

def get_degree_diff(points):

        first,second = points[0], points[1]

        first_q = [first.x, first.y,
                  first.z, first.w]
        second_q = [second.x, second.y,
                     second.z, second.w]

        delta_q = quaternion_multiply(first_q, quaternion_inverse(second_q))
        (_, _, yaw) = euler_from_quaternion(delta_q)

        return degrees(yaw)

def get_degrees_server():
    rospy.init_node('get_degree_diff_server')
    pub = rospy.Publisher("/")
    rospy.spin()

if __name__ == "__main__":
    get_degrees_server()
