import vex
from stddefs import *

global brain
brain = vex.Brain()
global master
master = vex.Controller()

# Right Drive
global drive_r1
drive_r1 = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO_6_1, False)
global drive_r2
drive_r2 = vex.Motor(vex.Ports.PORT2, vex.GearSetting.RATIO_6_1, False)
global drive_r3
drive_r3 = vex.Motor(vex.Ports.PORT3, vex.GearSetting.RATIO_6_1, False)
global drive_r4
drive_r4 = vex.Motor(vex.Ports.PORT4, vex.GearSetting.RATIO_6_1, False)

global drive_r
drive_r = vex.MotorGroup(drive_r1, drive_r2, drive_r3, drive_r4);

# Left Drive
global drive_l1
drive_l1 = vex.Motor(vex.Ports.PORT5, vex.GearSetting.RATIO_6_1, True)
global drive_l2
drive_l2 = vex.Motor(vex.Ports.PORT6, vex.GearSetting.RATIO_6_1, True)
global drive_l3
drive_l3 = vex.Motor(vex.Ports.PORT7, vex.GearSetting.RATIO_6_1, True)
global drive_l4
drive_l4 = vex.Motor(vex.Ports.PORT8, vex.GearSetting.RATIO_6_1, True)

global drive_l
drive_l = vex.MotorGroup(drive_l1, drive_l2, drive_l3, drive_l4);

# Subsystem 3
global intake
intake = vex.Motor(vex.Ports.PORT9, vex.GearSetting.RATIO_18_1, False);
global hang
hang = vex.Motor(vex.Ports.PORT10, vex.GearSetting.RATIO_36_1, False);

# Cylinders
global wing_r
wing_r = vex.DigitalOut(brain.three_wire_port.a)
global wing_l
wing_l = vex.DigitalOut(brain.three_wire_port.b)
global intake_fold
intake_fold = vex.DigitalOut(brain.three_wire_port.c)

# Sensors
global imu
imu = vex.Inertial(vex.Ports.PORT11)
global clock
clock = vex.Timer()
global auton_selector
auton_selector = vex.DigitalIn(brain.three_wire_port.h)

# Globals
global all_globals
all_globals = TrackedGlobals(0, 10.75, (3600 / 3593.6))
