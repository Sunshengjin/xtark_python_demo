#!/usr/bin/env python
# coding=utf-8 
"""
    xtark_python_demo/get_voltage.py - Version 1.0 @XTARK
       
    Copyright (c) 2020 XTARK.  All rights reserved.

    ·XMiddleWare接口库(XTARK机器人接口库)
    ·--IMU数据接口:  GetBattery()
<<<<<<< HEAD
    ·--返回数据格式(double)： 电池电压值(V)
=======
    ·--返回数据格式(double)： 电池电压值
>>>>>>> 1e265f7e0b9079c6682581eb9c09cad13d718bef

"""
import XMiddleWare as xmw #导入XMiddleWare  XTARK机器人接口库
import time

robot = xmw.XMiddleWare("/dev/ttyTHS1",115200)  # 建立 XTARK 机器人连接对象
robot.Init()                                    # 初始化 XTARK 机器人连接
print("Connecting Robot!")
time.sleep(1)                                   # 延时等待连接稳定
try:
    while True:
        bat = robot.GetBattery()                # 获取电池数据，返回电池电压浮点数
        print(" ")
        print("Voltage: %.3f" % (bat))          # 打印电池电压
        time.sleep(0.05)
except KeyboardInterrupt:
    pass
