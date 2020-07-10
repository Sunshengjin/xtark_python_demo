#!/usr/bin/env python
# coding=utf-8 
"""
    xtark_python_demo/get_odom.py - Version 1.0 @XTARK
    
    Copyright (c) 2020 XTARK.  All rights reserved.

    ·XMiddleWare接口库(XTARK机器人接口库)
    ·--Odom里程计数据接口:  GetOdom()
<<<<<<< HEAD
    ·--返回数据格式(list)： [里程计X坐标(m)，里程计Y坐标(m)，里程计Yaw角度(rad)，机器人X轴线速度(m/s)，机器人Y轴线速度(m/s)，机器人Yaw轴角度(rad/s)]
=======
    ·--返回数据格式(list)： [里程计X坐标，里程计Y坐标，里程计Yaw角度，机器人X轴线速度，机器人Y轴线速度，机器人Yaw轴角度]
>>>>>>> 1e265f7e0b9079c6682581eb9c09cad13d718bef

"""
import XMiddleWare as xmw   #导入XMiddleWare XTARK机器人接口库
import time

robot = xmw.XMiddleWare("/dev/ttyTHS1",115200) # 建立 XTARK 机器人连接对象
robot.Init()                                   # 初始化 XTARK 机器人连接 
print("Connecting Robot!")
time.sleep(1)
robot.SetParams(robot_type=0)                  # 设置默认机器人参数，清零里程计计数
time.sleep(1)                                  # 延时等待连接稳定
try:
    while True:
        odom = robot.GetOdom()                 # 获取Odom里程计数据，返回list()
                                               # 返回数据格式(list)： [里程计X坐标，里程计Y坐标，里程计Yaw角度，机器人X轴线速度，机器人Y轴线速度，机器人Yaw轴角度]
        print(" ")
        print("Odom_posX: %.3f,  Odom_posY: %.3f,  Odom_posYaw: %.3f" % (odom[0],odom[1],odom[2]))  # 打印里程计定位坐标数据
        print("Odom_vX:   %.3f,  Odom_vY:   %.3f,  Odom_vYaw:   %.3f" % (odom[3],odom[4],odom[5]))  # 打印里程计线速度数据
        time.sleep(0.05)
except KeyboardInterrupt:
    pass

