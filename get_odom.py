#!/usr/bin/env python
"""
    xtark_python_demo/get_odom.py - Version 1.0 @XTARK

"""
import XMiddleWare as xmw
import time

robot = xmw.XMiddleWare("/dev/ttyTHS1",115200)
robot.Init()
print("Connecting Robot!")
time.sleep(1)
robot.SetParams(robot_type=0)
time.sleep(1)
try:
    while True:
        odom = robot.GetOdom()
        print(" ")
        print("Odom_posX: %.3f,  Odom_posY: %.3f,  Odom_posYaw: %.3f" % (odom[0],odom[1],odom[2]))
        print("Odom_vX:   %.3f,  Odom_vY:   %.3f,  Odom_vYaw:   %.3f" % (odom[3],odom[4],odom[5]))
        time.sleep(0.05)
except KeyboardInterrupt:
    pass

