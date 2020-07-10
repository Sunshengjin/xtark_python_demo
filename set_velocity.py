#!/usr/bin/env python
# coding=utf-8 
"""
    xtark_python_demo/set_velocity.py - Version 1.0 @XTARK
    
    Copyright (c) 2020 XTARK.  All rights reserved.

    ·XMiddleWare接口库(XTARK机器人接口库)
    ·--速度控制接口:  SetVelocity(X轴线速度，Y轴线速度，Yaw轴角速度)
    ·--速度单位： X轴线速度：m/s  Y轴线速度: m/s Yaw轴角速度: rad/s

"""
import XMiddleWare as xmw    #导入XMiddleWare  XTARK机器人接口库
import time
import sys

robot = xmw.XMiddleWare("/dev/ttyTHS1",115200)  # 建立 XTARK 机器人连接对象
robot.Init()                                    # 初始化 XTARK 机器人连接
print("Connecting Robot!")
time.sleep(1)                                   # 延时等待连接稳定

print("Set Speed: x: 0.5m/s y: 0.0m/s yaw: 0.0rad/s")
robot.SetVelocity(0.5,0,0)                      # 设置机器人速度
time.sleep(1)
print("Stop Robot!")
robot.SetVelocity(0,0,0)
time.sleep(1)
print("Set Speed: x: 0.0m/s y: 0.5m/s yaw: 0.0rad/s")
robot.SetVelocity(0,0.5,0)
time.sleep(1)
print("Stop Robot!")
robot.SetVelocity(0,0,0)
time.sleep(1)
print("Set Speed: x: 0.0m/s y: 0.0m/s yaw: 1.0rad/s")
robot.SetVelocity(0,0,1.0)
time.sleep(1)
print("Stop Robot!")
robot.SetVelocity(0,0,0)
pass
