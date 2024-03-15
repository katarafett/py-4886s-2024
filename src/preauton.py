import vex
from robot_config import *

def preauton():
    brain.screen.clear_screen()
    imu.calibrate()

    while imu.is_calibrating():
        vex.wait(20, vex.TimeUnits.MSEC)
