#!/usr/bin/env python3
"""This setup node is responsible for drawing all the waypoints for the turtle sim"""

# Import the standard ROS message used in the service
from std_msgs.msg import Empty
from turtlesim.msg import _Pose
# Import the custom service "draw" we created
from homework2.srv import Draw, DrawRequest, DrawResponse
from std_srvs.srv import Empty
from turtlesim.srv import Spawn, SpawnRequest, SetPen, TeleportAbsolute, Kill
#from turtle_waypoint_following.srv import Draw, DrawResponse, DrawRequest
# import standar "rospy" API
import rospy
import rosparam
import yaml
import os
import time


class setup:
    
    def __init__(self):
        # The service resets the turtle sim and  clears all drawing
        
        #self.kill = rospy.ServiceProxy("/kill", Kill)
        #self.reset()
        self.draw_waypoint_service = rospy.Service("draw", Draw, self.callback_service
        # # The service draws all waypoints using an X shape
        # # Load all waypoints from the 'yaml' file
        waypoint_path = '/home/killian/catkin_ws/src/homework2/config/waypoint.yaml'
        way_points = rosparam.load_file(waypoint_path)
        rospy.loginfo("Waypoints are: {}". format(way_points[0][0]['waypoint']['waypoints']))
        self.waypoint_list  = way_points[0][0]['waypoint']['waypoints']
        print(self.waypoint_list[0])

        # place service request for waypoint maping
        #rospy.wait_for_service("draw")
        self.draw_waypoints = rospy.ServiceProxy("draw", Draw)
        #draw_waypoints()

        # # Let's create service for teleport and setting the pen to draw
        rospy.wait_for_service("/turtle1/set_pen")
        rospy.wait_for_service("/turtle1/teleport_absolute")
        self.setting_pen = rospy.ServiceProxy('/turtle1/set_pen', SetPen)
        #sett = setting_pen(0, 0 , 0, 50, 0)
        #time.sleep(3)
        self.resT =rospy.ServiceProxy('/turtle1/teleport_absolute',TeleportAbsolute)
        #resT2 = resT(4,3,0)
        #time.sleep(3)
        #rospy.wait_for_service("kill")
        #clear = rospy.ServiceProxy("/turtle1/kill", Kill)

        #clear()
        #sett = setting_pen(0, 0 , 0, 1, 1)
        #self.teleport_turtle1(3, 3, 0)
        def callback_service(self)
            margin = 0.1
            for iter in range(len(self.waypoint_list)-1, -1, -1):
                point = self.waypoint_list[iter]
                print("kkkkkk", point[0])
                setting_pen(0, 0 , 0, 1, 1)
                resT(point[0] + margin, point[1]+margin, 0)
                setting_pen(0, 0 , 0, 1, 0)
                resT(point[0]-margin, point[1]-margin, 0)
                setting_pen(0, 0 , 0, 1, 1)
                resT(point[0]+margin, point[1]-margin, 0)
                setting_pen(0, 0 , 0, 1, 0)
                resT(point[0]-margin, point[1]+margin, 0)

                resT(point[0], point[1], 0)
                rospy.sleep(2)


        



def main():
    rospy.init_node("draw_node", log_level=rospy.DEBUG, anonymous=True)
    rospy.wait_for_service('reset')
    clear_bg = rospy.ServiceProxy('reset', Empty)
    clear_bg()
    setup()
    time.sleep(1)
    rospy.spin()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass


