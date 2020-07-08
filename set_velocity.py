#!/usr/bin/env python
"""
    xtark_python_demo/set_velocity.py - Version 1.0 @XTARK

"""
import XMiddleWare as xmw
import time
import sys

robot = xmw.XMiddleWare("/dev/ttyTHS1",115200)
robot.Init()
print("Connecting Robot!")
time.sleep(1)

print("Set Speed: x: 0.5m/s y: 0.0m/s yaw: 0.0rad/s")
robot.SetVelocity(0.5,0,0)
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
