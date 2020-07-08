#!/usr/bin/env python
"""
    xtark_python_demo/run_teleop.py - Version 1.0 @XTARK
    
    Copyright (c) 2020 XTARK.  All rights reserved.

    ·XMiddleWare接口库(XTARK机器人接口库)
    ·--例程：机器人键盘控制移动简单实现
    
"""

import sys, select, termios, tty,time

import XMiddleWare as xmw   #导入XMiddleWare  XTARK机器人接口库

# 提示信息打印
msg = """                                                      
Reading from the keyboard  and ControlRobot!
---------------------------
Moving around:
   u    i    o         ^
   j    k    l       < v >
   m    ,    .

For Holonomic mode (strafing), hold down the shift key:
---------------------------
   U    I    O
   J    K    L
   M    <    >

t : up (+z)
b : down (-z)

anything else : stop

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%

CTRL-C to quit
"""

moveBindings = {            #移动控制键位绑定表
        'i':(1,0,0,0),
        'o':(1,0,0,-1),
        'j':(0,0,0,1),
        'l':(0,0,0,-1),
        'u':(1,0,0,1),
        ',':(-1,0,0,0),
        '.':(-1,0,0,1),
        'm':(-1,0,0,-1),
        'O':(1,-1,0,0),
        'I':(1,0,0,0),
        'J':(0,1,0,0),
        'L':(0,-1,0,0),
        'U':(1,1,0,0),
        '<':(-1,0,0,0),
        '>':(-1,-1,0,0),
        'M':(-1,1,0,0),
        't':(0,0,1,0),
        'b':(0,0,-1,0),
        'A':(1,0,0,0),
        'B':(-1,0,0,0),
        'C':(0,0,0,-1),
        'D':(0,0,0,1),
    }

speedBindings={            #速度大小控制键位绑定表
        'q':(1.1,1.1),
        'z':(.9,.9),
        'w':(1.1,1),
        'x':(.9,1),
        'e':(1,1.1),
        'c':(1,.9),
    }

def getKey():                               #读取键盘输入函数
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


def vels(speed,turn):
    return "currently:\tspeed %s\tturn %s " % (speed,turn)

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)
    speed = 0.5
    turn  = 1.0
    x = 0
    y = 0
    z = 0
    th = 0
    status = 0

    robot = xmw.XMiddleWare("/dev/ttyTHS1",115200)      # 建立 XTARK 机器人连接对象
    robot.Init()                                        # 初始化 XTARK 机器人连接
    time.sleep(0.5)                                     # 延时等待连接稳定


    try:
        print(msg)
        print(vels(speed,turn))
        while(1):
            key = getKey()                              # 获取键盘输入
            if key in moveBindings.keys():              # 查询输入键位是否为移动控制
                x = moveBindings[key][0]
                y = moveBindings[key][1]
                z = moveBindings[key][2]
                th = moveBindings[key][3]
            elif key in speedBindings.keys():           # 查询输入键位是否为速度增减控制
                speed = speed * speedBindings[key][0]
                turn = turn * speedBindings[key][1]

                print(vels(speed,turn))
                if (status == 14):
                    print(msg)
                status = (status + 1) % 15
            else:                                       # 查询不匹配，停止机器人
                x = 0
                y = 0
                z = 0
                th = 0
                if (key == '\x03'):
                    break
            
            robot.SetVelocity(x*speed,y*speed,th*turn)  # 根据键位输入移动机器人
    
    except Exception as e:
        print(e)

    finally:
        robot.SetVelocity(0,0,0)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
