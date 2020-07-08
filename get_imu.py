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
        imu = robot.GetIMU()
        print("  ")
        print("Gyro_roll: %.3f,   Gyro_pitch: %.3f,  Gyro_yaw: %.3f" % (imu[0],imu[1],imu[2]))
        print("Acc_x: %.3f,        Acc_y: %.3f,      Acc_z: %.3f" % (imu[3],imu[4],imu[5]))
        print("Angle_roll: %.3f,  Acc_pitch: %.3f,  Acc_yaw: %.3f" % (imu[6],imu[7],imu[8]))
        time.sleep(0.05)

except KeyboardInterrupt:
    pass


