#!/usr/bin/env python
"""
    xtark_python_demo/run_square.py - Version 1.0 XTARK


"""
import XMiddleWare as xmw
import time

robot = xmw.XMiddleWare("/dev/ttyTHS1",115200)
robot.Init()
print(" Connecting Robot!")
time.sleep(1)
robot.SetParams(robot_type=0)
time.sleep(1)


step_group = list()
step_group.append([1.0 ,1.0 , 0])
step_group.append([-1.0 , 0 , 0])
step_group.append([1.0 ,-1.0 , 0])
step_group.append([-1.0 , 0 , 0])

linear_tolerance = 0.1
angular_tolerance = 0.2

linear_speed = 0.3
angular_speed = 1.0

x_speed = 0.0
y_speed = 0.0
yaw_speed = 0.0

odom = robot.GetOdom()

for current_step in step_group:
    print("Current Step: ",current_step)
    current_goal_x   = odom[0]+current_step[0]
    current_goal_y   = odom[1]+current_step[1]
    current_goal_yaw = odom[2]+current_step[2]
    while True:
        x_speed   = ((current_goal_x - odom[0])>0 and 1 or -1)*((abs(current_goal_x - odom[0]) > linear_tolerance) and linear_speed or 0) 
        y_speed   = ((current_goal_y - odom[1])>0 and 1 or -1)*((abs(current_goal_y - odom[1]) > linear_tolerance) and linear_speed or 0) 
        yaw_speed = ((current_goal_yaw - odom[2])>0 and 1 or -1)*((abs(current_goal_yaw - odom[2]) > angular_tolerance) and angular_speed or 0) 
        robot.SetVelocity(x_speed,y_speed,yaw_speed)
        odom = robot.GetOdom()
        time.sleep(0.04)
        if((x_speed == 0) and (y_speed == 0) and (yaw_speed == 0)):
            robot.SetVelocity(0,0,0)
            time.sleep(1)
            break

print("All Step Reached!")
pass

