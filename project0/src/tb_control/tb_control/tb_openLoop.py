#!/usr/bin/env python

import rclpy
import rclpy.exceptions
import rclpy.logging
from rclpy.node import Node
from geometry_msgs.msg import Twist

MAX_VELOCITY = 1.0  # maximum velocity of robot
TARGET_DISTANCE = float(input("Enter Distance: "))  # distance to cover
ACCELERATION = 0.25  # acceleration
TIME_STEP = 0.2  # time in seconds between updating the velocity
INITIAL_VELOCITY = 0.0
SCENARIO = input("Enter scenario number: ")


class VelocityPublisher(Node):
    def __init__(self):
        super().__init__("velocity_publisher")
        self.publisher = self.create_publisher(Twist, "cmd_vel", 1)
        self.distance_covered = 0  # distance covered by robot when at constant velocity
        self.wait_time = TIME_STEP  # time between two call backs on get velocity
        self.current_velocity = INITIAL_VELOCITY
        self.timer = self.create_timer(self.wait_time, self.get_velocity)

    def publish_velocity(self, velocity):
        twist = Twist()
        twist.linear.x = velocity
        self.publisher.publish(twist)
        self.get_logger().info("Velocity:" + str(twist.linear.x))

    def get_velocity(self):
        remaning_distance = TARGET_DISTANCE - self.distance_covered
        if SCENARIO == "1":  # SCENARIO == 1
            if remaning_distance > 0.0:
                self.current_velocity = MAX_VELOCITY
            else:
                self.current_velocity = 0.0
            self.distance_covered = round(
                self.distance_covered + self.current_velocity * TIME_STEP, 2
            )

        else:  # SCENARIO == 2
            if (
                remaning_distance <= (self.current_velocity**2) / (2 * ACCELERATION)
            ):  # condition to check when to decelerate. The remaining distance should be enough for the robot to come to rest at target position.
                # decelerate
                new_velocity = round(
                    self.current_velocity - ACCELERATION * TIME_STEP, 2
                )
                self.current_velocity = max(0.0, new_velocity) #If calulated new velocity goes negative, we will chose 0 as velocity as we dont want robot to move backward. Otherwise use calculated velocity.

            else:  # condition to check when to accelerate
                # accelerate
                new_velocity = round(
                    self.current_velocity + ACCELERATION * TIME_STEP, 2
                )
                self.current_velocity = min(new_velocity, MAX_VELOCITY) #If calulated new velocity goes above max velocity, we will chose max velocity as velocity as we cant go faster than max velocity.Otherwise use calculated velocity.

            # maintain contsant velocity and count distance traveled
            self.distance_covered = round(
                self.distance_covered + self.current_velocity * TIME_STEP, 2
            )

        self.publish_velocity(self.current_velocity)  #Publishing the velocity


def main(args=None):
    rclpy.init(args=args)           #Initializing
    publish = VelocityPublisher()   #Creating instance of node
    rclpy.spin(publish)             # Running the node


if __name__ == "__main__":
    try:
        main()
    except Exception:
        raise rclpy.exceptions.ROSInterruptException
