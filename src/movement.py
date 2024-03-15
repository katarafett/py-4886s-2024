from robot_config import *
from pid import Pid
from util import *
import vex

# takes inches, target inches per second (velocity),
# inches per second squared (acceleration), and whether to decelerate
def drive_straight(inches, target_ips, ipss, do_decel = True):
    # PID constants
    DR_KP = 0.005
    DR_KI = 0.00
    DR_KD = 1.9

    DL_KP = 0.005
    DL_KI = 0.00
    DL_KD = 1.9

    DIR_KP = 2.925
    DIR_KI = 0.00
    DIR_KD = 0.183

    # Loop wait times
    TPS = 50    # tick per sec
    MSPT = 20   # ms per tick

    MULTIPLIER = 1.2        # not sure why I need this, but it makes it so that
    inches *= MULTIPLIER    # passing 4 inches actually moves 4 inches

    drive_r.stop(COAST)
    drive_l.stop(COAST)

    pid_drive_r = Pid(DR_KP, DR_KI, DR_KD)
    pid_drive_l = Pid(DL_KP, DL_KI, DL_KD)
    pid_dir = Pid(DIR_KP, DIR_KI, DIR_KD)

    ips = 0     # current speed in ips
    expected_pos = 0     # inches travelled since function call
    pos_start_l = drive_l.position(REV)
    pos_start_r = drive_r.position(REV)

    # adjusts velocity for positive/negative distances
    dir_mod = 1 if inches < 0 else -1

    # While speed is positive and we haven't gone further than `inches`
    while ips >= 0 and abs(pos_drive_l() - pos_start_l) < abs(inches):
        # Handle acceleration
        if abs(expected_pos) + stop_distance(ips, ipss) >= abs(inches) and do_decel:
            ips -= ipss / TPS           # decel
        elif ips < target_ips:
            ips += target_ips / TPS     # accel
        else:
            ips = target_ips            # cap vel at target_ips

        # Find expected position
        expected_pos += ips / TPS * dir_mod      # dir_mod adjusts for moving fwd/bwd

        # Find actual position
        pos_l = pos_drive_l() - pos_start_l
        pos_r = pos_drive_r() - pos_start_r

        adjustment_r = pid_drive_r.adjust(expected_pos, pos_l)
        adjustment_l = pid_drive_l.adjust(expected_pos, pos_l)
        adjustment_dir = pid_dir.adjust(all_globals.target_heading, pos_l)
