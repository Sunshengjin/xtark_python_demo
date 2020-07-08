#!/usr/bin/env python
"""
    xtark_python_demo/get_imu.py - Version 1.0 @XTARK


"""
import XMiddleWare as xmw
import time

robot = xmw.XMiddleWare("/dev/ttyTHS1",115200)
robot.Init()
print("Connecting Robot!")
time.sleep(1)
try:
    while True:
        bat = robot.GetBattery()
        print(" ")
        print("Voltage: %.3f" % (bat))
        time.sleep(0.05)
except KeyboardInterrupt:
    pass
