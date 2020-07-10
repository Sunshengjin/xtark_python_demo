#!/usr/bin/env python
# coding=utf-8 
"""
    xtark_python_demo/run_position.py
    
    Copyright (c) 2020 XTARK.  All rights reserved.

    ·XMiddleWare接口库(XTARK机器人接口库)
    ·--例程：利用速度设置接口SetVelocity()以及里程计获取接口，实现机器人简单位置闭环控制
            通过添加运动步骤列表（X轴前进里程（m），Y轴前进里程（m),Yaw轴旋转角度（rad）） 实现机器人位置运动控制
            此里程为控制机器人运动X型轨迹

"""
import XMiddleWare as xmw    # 导入XMiddleWare  XTARK机器人接口库
import time

robot = xmw.XMiddleWare("/dev/ttyTHS1",115200)  # 建立 XTARK 机器人连接对象
robot.Init()                                    # 初始化 XTARK 机器人连接
print(" Connecting Robot!")
time.sleep(1)
robot.SetParams(robot_type=0)                   # 初始化机器人里程计，并设置机器人为麦克纳姆轮
time.sleep(1)


step_group = list()                             # 运动步骤 列表
step_group.append([1.0 ,1.0 , 0])               # 添加一个运动步骤，向X轴正方向运动1m，同时向Y轴正方向运动1m
step_group.append([-1.0 , 0 , 0])               # 添加一个运动步骤，向X轴负方向运动1m
step_group.append([1.0 ,-1.0 , 0])              # 添加一个运动步骤，向X轴正方向运动1m，同时向Y轴负方向运动1m
step_group.append([-1.0 , 0 , 0])               # 添加一个运动步骤，向X轴负方向运动1m

linear_tolerance = 0.1                          # 运动线里程允许误差
angular_tolerance = 0.2                         # 运动角度允许误差

linear_speed = 0.3                              # 运动线速度
angular_speed = 1.0                             # 运动角速度

x_speed = 0.0
y_speed = 0.0
yaw_speed = 0.0

odom = robot.GetOdom()

for current_step in step_group:                 # 控制机器人一步一步执行运动步骤
    print("Current Step: ",current_step)
    current_goal_x   = odom[0]+current_step[0]
    current_goal_y   = odom[1]+current_step[1]
    current_goal_yaw = odom[2]+current_step[2]
    while True:
        x_speed   = ((current_goal_x - odom[0])>0 and 1 or -1)*((abs(current_goal_x - odom[0]) > linear_tolerance) and linear_speed or 0)    #通过里程计，实现运动里程闭环控制
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

