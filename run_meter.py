#!/usr/bin/env python
"""
    xtark_python_demo/run_meter.py - Version 1.0 @XTARK

"""
import XMiddleWare as xmw
import time

robot = xmw.XMiddleWare("/dev/ttyTHS1",115200)
robot.Init()
time.sleep(1)

time_count = 0

while(time_count < 20):
    robot.SetVelocity(0.5,0,0)
    time_count = time_count+1
    time.sleep(0.05)

robot.SetVelocity(0,0,0)
time.sleep(1)
pass


