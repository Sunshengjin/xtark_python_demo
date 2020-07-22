#!/usr/bin/env python
# coding=utf-8  
"""
    xtark_python_demo/get_wheelspeed.py - Version 1.0 @XTARK
    
    Copyright (c) 2020 XTARK.  All rights reserved.

    ·XMiddleWare接口库(XTARK机器人接口库)
    ·--轮子转速获取接口:  GetWheelSpeed()
    ·--返回数据格式(list)： [A轮转速，B轮转速，C轮转速，D轮转速]
    ·--速度单位： 一个PID周期（25Hz）轮子编码器计数变化值

"""
import XMiddleWare as xmw   #导入XMiddleWare XTARK机器人接口库
import time

robot = xmw.XMiddleWare("/dev/ttyAMA0",115200) # 建立 XTARK 机器人连接对象
robot.Init()                                   # 初始化 XTARK 机器人连接 
print("Connecting Robot!")
time.sleep(1)
robot.SetParams()                  # 设置默认机器人参数，清零里程计计数
time.sleep(1)                                  # 延时等待连接稳定
try:
    while True:
        wheelspeed = robot.GetWheelSpeed()                 # 获取轮子转速数据，返回list()
                                               # 返回数据格式(list)： [A轮转速，B轮转速，C轮转速，D轮转速]
        print(" ")
        print("WheelSpeed: A: %d,  B: %d,  C: %d,  D: %d" % (wheelspeed[0],wheelspeed[1],wheelspeed[2],wheelspeed[3]))  # 打印里程计定位坐标数据
        time.sleep(0.05)
except KeyboardInterrupt:
    pass

