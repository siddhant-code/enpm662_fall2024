# Project 0

The package provided here is intended to handle two scenarios based on user input:

## Scenario 1
The Turtle bot is expected to move a user-defined distance with constant velocity.

## Scenario 2
The Turtle bot is expected to move a user-defined distance starting from rest, accelerating to a peak velocity, continuing at peak velocity for certain distance, and then decelerating to rest.

## Defined Values
For this project, we have defined the following values for the robot:

- **Max velocity:** 1 m/s
- **Acceleration:** 0.25 m/s²

Since the robot is moving forward in a single direction, in this particular case, distance and displacement are equal, and the terms can be used interchangably.

## Use the following command to run the node
ros2 run tb_control tb_openloop

## Input
After running the node, it will ask for two inputs:

1. Distance to be travelled
2. Scenario number

The velocity can be monitored through logs printed by the node.
