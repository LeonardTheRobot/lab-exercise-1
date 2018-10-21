#!/usr/bin/env python
import rospy
import numpy as np

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class WallHugger:
    def __init__(self):
        rospy.Subscriber('base_scan', LaserScan, self.laser_callback)
        self.movement_publisher = rospy.Publisher('cmd_vel', Twist, queue_size=100)

        self.lin_speed = 0.6
        self.ang_speed = 0.75
        target_wall_distance = 1.0 # 1.0m
        wall_hug_accuracy = 0.1 # +/- 0.1m
        self.min_wall_distance = target_wall_distance - wall_hug_accuracy
        self.max_wall_distance = target_wall_distance + wall_hug_accuracy

    def laser_callback(self, laser_msg):
        # Array of all sensor readings ordered from right to left as per API
        laser_readings = np.array(laser_msg.ranges)
        # Split into 3 equal arrays of left, front and right laser readings
        rights, fronts, lefts = np.split(laser_readings, 3)
        # rospy.loginfo('L: {}, F: {}, R: {}'.format(lefts, fronts, rights))

        left = np.sort(lefts)[10]
        front = np.sort(fronts)[10]
        right = np.sort(rights)[10]
        rospy.loginfo('L: {}, F: {}, R: {}'.format(left, front, right))

        new_speed = Twist()

        if front < 1.0 * self.min_wall_distance or min(laser_readings) < 0.5 * self.min_wall_distance:
            rospy.loginfo('OBSTRUCTED')
            new_speed.angular.z = self.ang_speed
        else:
            new_speed.linear.x = self.lin_speed

            if right < self.min_wall_distance:
                rospy.loginfo('TOO CLOSE')
                new_speed.angular.z = self.ang_speed
            elif right > self.max_wall_distance:
                rospy.loginfo('TOO FAR')
                new_speed.angular.z = -self.ang_speed
        rospy.loginfo('lin: {}, ang: {}'.format(new_speed.linear.x, new_speed.angular.z))
        self.movement_publisher.publish(new_speed)

if __name__ == '__main__':
    rospy.init_node(name='wall_hugger')
    raw_input('Switch on motors, then press Enter to start...')
    wall_hugger = WallHugger()
    rospy.spin()
