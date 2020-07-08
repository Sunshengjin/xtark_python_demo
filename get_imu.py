#!/usr/bin/env python
# coding=utf-8 
"""
    xtark_python_demo/get_imu.py - Version 1.0 @XTARK
    
    Copyright (c) 2020 XTARK.  All rights reserved.

    ·XMiddleWare接口库(XTARK机器人接口库)
    ·--IMU数据接口:  GetIMU()
    ·--返回数据格式(list)： [陀螺仪Roll，陀螺仪Pitch，陀螺仪Yaw，线加速度X，线加速度Y，线加速度Z，姿态角Roll，姿态角Pitch，姿态角Yaw]
    
"""
import XMiddleWare as xmw #导入XMiddleWare  XTARK机器人接口库
import time         

robot = xmw.XMiddleWare("/dev/ttyTHS1",115200) # 建立 XTARK 机器人连接对象
robot.Init()                                   # 初始化 XTARK 机器人连接
print("Connecting Robot!")
time.sleep(1)                                  # 延时等待连接稳定
try:
    while True:
        imu = robot.GetIMU()                   # 获取IMU数据，返回list()
                                               # 数据格式： [陀螺仪Roll，陀螺仪Pitch，陀螺仪Yaw，线加速度X，线加速度Y，线加速度Z，姿态角Roll，姿态角Pitch，姿态角Yaw]
        print("  ")
        print("Gyro_roll: %.3f,   Gyro_pitch: %.3f,  Gyro_yaw: %.3f" % (imu[0],imu[1],imu[2])) # 打印陀螺仪数据
        print("Acc_x: %.3f,        Acc_y: %.3f,      Acc_z: %.3f" % (imu[3],imu[4],imu[5]))    # 打印线加速度数据
        print("Angle_roll: %.3f,  Acc_pitch: %.3f,  Acc_yaw: %.3f" % (imu[6],imu[7],imu[8]))   # 打印角度数据
        time.sleep(0.05)

except KeyboardInterrupt:
    pass


