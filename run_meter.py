#!/usr/bin/env python
# coding=utf-8 
"""
    xtark_python_demo/run_meter.py - Version 1.0 @XTARK

    Copyright (c) 2020 XTARK.  All rights reserved.

    ·XMiddleWare接口库(XTARK机器人接口库)
    ·--例程：利用速度控制接口SetVelocity(x, y, yaw)以及延时函数，实现机器人前进距离/时间控制
    
    OpenCRP内置多种底盘运动学算法，可直接输入三轴速度，底层自动解析，实现多种底盘运动模式（默认为麦克纳姆轮运动模式）
    具体底盘类型设置及不同底盘运动学参数设置接口，详见set_params.py例程
"""
import XMiddleWare as xmw #导入XMiddleWare  XTARK机器人接口库
import time

robot = xmw.XMiddleWare("/dev/ttyAMA0",115200)  # 建立 XTARK 机器人连接对象
robot.Init()                                    # 初始化 XTARK 机器人连接
time.sleep(1)

time_count = 0

while(time_count < 40):                         # 每次循环延时0.05s, 循环40次，即运行2s
    robot.SetVelocity(0.5,0,0)                  # 调用速度设置接口，直接控制底盘三轴速度。即 (X轴线速度(m/s)，Y轴线速度(m/s)，Yaw轴角速度(rad/s))
    time_count = time_count+1                   # 以0.5m/s运行2s，机器人大致前进1m
    time.sleep(0.05)

robot.SetVelocity(0,0,0)                        # 将机器人三轴速度设置为0，停止机器人
time.sleep(1)
pass


