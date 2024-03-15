import vex
from robot_config import *
import util

# Constants
TNK = 0
TSA = 1
OSA = 2

def opcontrol():
    SENSITIVITY = 0.85

    # Set up edge detection
    fold_switch = util.EdgeDetection(False)
    wing_r_switch = util.EdgeDetection(False)
    wing_l_switch = util.EdgeDetection(False)
    hang_switch = util.EdgeDetection(False)

    # Reset drive velocity
    drive_l.stop(vex.BrakeType.COAST)
    drive_r.stop(vex.BrakeType.COAST)

    while(True):
        opdrive(TSA, 1.0, SENSITIVITY)

        # Set a "shift" key
        shifted = master.buttonL2.pressing()

        # Base layer
        if not shifted:
            # Intake
            intake.spin(FORWARD, (master.buttonR1.pressing() - master.buttonR2.pressing()) * 100, vex.VelocityPercentUnits)
            # Change intake height
            intake_fold.set(fold_switch.is_redge(master.buttonL1.pressing()))

        # Shifted layer
        if shifted:
            # Wings
            wing_l.set(wing_l_switch.is_redge(master.buttonL1.pressing()))
            wing_r.set(wing_r_switch.is_redge(master.buttonR1.pressing()))
        # y hang

def opdrive(control_scheme, speed_mod, turn_mod):
    axis_rx = master.axis1.value()
    axis_ry = master.axis2.value()
    axis_lx = master.axis3.value()
    axis_ly = master.axis4.value()
    # Tank drive
    if control_scheme == TNK:
        drive_r.spin(FORWARD, axis_ry * speed_mod, vex.VelocityUnits.PERCENT)
        drive_l.spin(FORWARD, axis_lx * speed_mod, vex.VelocityUnits.PERCENT)
    elif control_scheme == TSA:
        drive_r.spin(FORWARD, (axis_lx - axis_rx * turn_mod) * speed_mod, vex.VelocityUnits.PERCENT)
        drive_l.spin(FORWARD, (axis_lx + axis_rx * turn_mod) * speed_mod, vex.VelocityUnits.PERCENT)
    elif control_scheme == OSA:
        drive_r.spin(FORWARD, (axis_ly - axis_lx * turn_mod) * speed_mod, vex.VelocityUnits.PERCENT)
        drive_l.spin(FORWARD, (axis_ly + axis_lx * turn_mod) * speed_mod, vex.VelocityUnits.PERCENT)
