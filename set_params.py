#!/usr/bin/env python
# coding=utf-8 
"""
    xtark_python_demo/set_params.py - Version 1.0 @XTARK

    Copyright (c) 2020 XTARK.  All rights reserved.

    ·XMiddleWare接口库(XTARK机器人接口库)
    ·--机器人运动学参数设置函数（SetParams()）
        OpenCRP内置多种底盘运动学模型，包括麦克纳姆轮，差速底盘，用户可通过此函数接口，配置各底盘运动学参数，以实现精确的运动以及里程计计算

        注：调用此接口时，会清空内部里程计计数，即初始化里程计传感器
        
    ·--设置参数列表:
        SetParams(encoder_resolution  ,  wheel_diameter  ,  robot_linear_acc  ,  robot_angular_acc  ,  wheel_track )
        -参数类型       int                  double               double               double             double          
        -参数意义   编码器分辨率             轮胎直径           机器人线加速度        机器人角加速度          左右轮距  
        -参数单位  编码器线数*减速比             m                   m/s2                 rad/s2               m            
    -是否必选(默认值)  可选(1440)            可选（0.097）         可选（1.5）           可选（3.0)         可选（0.3)  
"""
import XMiddleWare as xmw
import time

robot = xmw.XMiddleWare("/dev/ttyAMA0",115200)  # 导入XMiddleWare  XTARK机器人接口库
robot.Init()                                    # 建立 XTARK 机器人连接对象
print("Connecting Robot!")
time.sleep(1)                                   # 延时等待连接稳定
encoder_resolution_   = 1440                    # 设置底盘编码器分辨率
wheel_diameter_       = 0.097                   # 设置底盘轮径
robot_linear_acc_     = 1.5                     # 设置线加速度
robot_angular_acc_    = 2.0                     # 设置角加速度
wheel_track_          = 0.315                   # 设置轮距（差速地盘）
print("Set Robot Params: ")
print("--Set Encoder Resolution: %d " % (encoder_resolution_))
print("--Set Wheel_diameter:     %.3f" % (wheel_diameter_))
print("--Set Robot Linear Acc:   %.3f" % (robot_linear_acc_))
print("--Set Robot Angular Acc:  %.3f" % (robot_angular_acc_))
print("--Set Wheel Track:        %.3f" % (wheel_track_))

robot.SetParams(encoder_resolution=encoder_resolution_, wheel_diameter=wheel_diameter_, robot_linear_acc=robot_linear_acc_, robot_angular_acc=robot_angular_acc_, wheel_track=wheel_track_)

pass
