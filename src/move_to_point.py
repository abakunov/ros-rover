def move_to_point():
    start_position = robot_position

    rospy.init_node('splus_bot', anonymous=True)

    pub = rospy.Publisher('cmd_vel' , Twist, queue_size = 10)
    msg = Twist()
    msg.linear.x = 0.05
    pub.publish(msg)




    while start_position <= robot_position:
        pub.publish(msg)