from vex import *

def init():
    global brain
    brain = Brain()
    global master
    master = Controller()

    # Right Drive
    global drive_r1
    drive_r1 = Motor(Ports.PORT1, GearSetting.RATIO_6_1, False)
    global drive_r2
    drive_r2 = Motor(Ports.PORT2, GearSetting.RATIO_6_1, False)
    global drive_r3
    drive_r3 = Motor(Ports.PORT3, GearSetting.RATIO_6_1, False)
    global drive_r4
    drive_r4 = Motor(Ports.PORT4, GearSetting.RATIO_6_1, False)

    global drive_r
    drive_r = MotorGroup(drive_r1, drive_r2, drive_r3, drive_r4);

    # Left Drive
    global drive_l1
    drive_l1 = Motor(Ports.PORT5, GearSetting.RATIO_6_1, True)
    global drive_l2
    drive_l2 = Motor(Ports.PORT6, GearSetting.RATIO_6_1, True)
    global drive_l3
    drive_l3 = Motor(Ports.PORT7, GearSetting.RATIO_6_1, True)
    global drive_l4
    drive_l4 = Motor(Ports.PORT8, GearSetting.RATIO_6_1, True)

    global drive_l
    drive_l = MotorGroup(drive_l1, drive_l2, drive_l3, drive_l4);

    # Subsystem 3
    global intake
    intake = Motor(Ports.PORT9, GearSetting.RATIO_18_1, False);
    global hang
    hang = Motor(Ports.PORT10, GearSetting.RATIO_36_1, False);

    # Wings
    global wing_r
    wing_r = DigitalOut(brain.three_wire_port.a)
    global wing_l
    wing_l = DigitalOut(brain.three_wire_port.b)

    # Sensors
    global imu
    imu = Inertial(Ports.PORT11)
    global clock
    clock = Timer()
    global auton_selector
    auton_selector = DigitalIn(brain.three_wire_port.a)
