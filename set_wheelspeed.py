#!/usr/bin/env python
# coding=utf-8 
"""
    xtark_python_demo/set_wheelspeed.py - Version 1.0 @XTARK
     
    Copyright (c) 2020 XTARK.  All rights reserved.

    ·XMiddleWare接口库(XTARK机器人接口库)
    ·--轮速设置接口:  SetWheelSpeed(A轮速度，B轮速度，C轮速度，D轮速度)
    ·--速度单位：  每PID周期（25hz）内轮子编码器期望变化值
    ·--此速度为PID闭环控制

"""
import XMiddleWare as xmw       #导入 XMiddleWare XTARK 机器人接口库
import time

robot = xmw.XMiddleWare("/dev/ttyAMA0",115200)          # 建立XTARK机器人连接对象
robot.Init()                                            # 初始化XTARK机器人连接
print("Connecting Robot!")
time.sleep(1)                                           # 延时等待连接稳定

print("Set Wheel Speed: a[50]  b[-50]  c[0]  d[0]")
robot.SetWheelSpeed(50,-50,0,0)                         # 设置轮子转速                       
time.sleep(1)
print("Set Wheel Speed: a[0]   b[50]  c[-50]  d[0]")
robot.SetWheelSpeed(0,50,-50,0)                         # 设置轮子转速
time.sleep(1)
print("Set Wheel Speed: a[0]   b[0]  c[50]  d[-50]")
robot.SetWheelSpeed(0,0,50,-50)                         # 设置轮子转速
time.sleep(1)
print("Set Wheel Speed: a[-50]   b[0]  c[0]   d[50]")
robot.SetWheelSpeed(-50,0,0,50)                         # 设置轮子转速
time.sleep(1)
print("Set Wheel Speed: a[0]   b[0]  c[0]   d[0]")
robot.SetWheelSpeed(0,0,0,0)                            # 设置轮子转速
time.sleep(1)
print("Set Wheel Speed: a[50]   b[50]  c[50]   d[50]")
robot.SetWheelSpeed(50,50,50,50)                        # 设置轮子转速
time.sleep(1)
print("Stop Robot!")
robot.SetWheelSpeed(0,0,0,0)                            # 停止
pass

