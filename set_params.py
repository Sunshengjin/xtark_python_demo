"""
    xtark_python_demo/set_params.py - Version 1.0 @XTARK


"""
import XMiddleWare as xmw
import time

robot = xmw.XMiddleWare("/dev/ttyTHS1",115200)
robot.Init()
print("Connecting Robot!")
time.sleep(1)
robot_type_           = 0
encoder_resolution_   = 1440
wheel_diameter_       = 0.097
robot_linear_acc_     = 1.5
robot_angular_acc_    = 2.0
wheel_track_          = 0.315
wheel_a_mec_          = 0.095
wheel_b_mec_          = 0.075
print("Set Robot Params: ")
print("--Set Robot Type:         %d  (0-Mecnum 1-Diff)" % (robot_type_))
print("--Set Encoder Resolution: %d " % (encoder_resolution_))
print("--Set Wheel_diameter:     %.3f" % (wheel_diameter_))
print("--Set Robot Linear Acc:   %.3f" % (robot_linear_acc_))
print("--Set Robot Angular Acc:  %.3f" % (robot_angular_acc_))
print("--Set Wheel Track:        %.3f" % (wheel_track_))
print("--Set Wheel A Mec:        %.3f" % (wheel_a_mec_))
print("--Set Wheel B Mec:        %.3f" % (wheel_b_mec_))

robot.SetParams(robot_type=robot_type_, encoder_resolution=encoder_resolution_, wheel_diameter=wheel_diameter_, robot_linear_acc=robot_linear_acc_, robot_angular_acc=robot_angular_acc_, wheel_track=wheel_track_, wheel_a_mec=wheel_a_mec_,wheel_b_mec=wheel_b_mec_)

pass
