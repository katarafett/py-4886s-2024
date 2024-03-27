from robot_config import *
from pid import Pid
from util import *
import vex

# takes inches, target inches per second (velocity),
# inches per second squared (acceleration), and whether to decelerate
def drive_straight(inches, target_ips, ipss, do_decel = True):
    # Loop vex.wait times
    TICK_PER_SEC = 50    # tick per sec
    MSEC_PER_TICK = 1000 / 20   # ms per tick

    # PID constants
    DRIVE_KP = 0.005
    DRIVE_KI = 0.00
    DRIVE_KD = 1.9

    DIR_KP = 2.925
    DIR_KI = 0.00
    DIR_KD = 0.183

    MULTIPLIER = 1.2        # not sure why I need this, but it makes it so that
    inches *= MULTIPLIER    # passing 4 inches actually moves 4 inches

    drive_r.stop(vex.COAST)
    drive_l.stop(vex.COAST)

    pid_drive_r = Pid(DRIVE_KP, DRIVE_KI, DRIVE_KD)
    pid_drive_l = Pid(DRIVE_KP, DRIVE_KI, DRIVE_KD)
    pid_dir = Pid(DIR_KP, DIR_KI, DIR_KD)

    ips = 0     # current speed in ips
    expected_displacement = 0     # inches travelled since function call
    pos_start_l = drive_l.position(REV)
    pos_start_r = drive_r.position(REV)

    # adjusts velocity for positive/negative distances
    dir_mod = 1 if inches < 0 else -1

    # While speed is positive and we haven't gone further than `inches`
    while ips >= 0 and abs(pos_drive_l() - pos_start_l) < abs(inches):
        # Handle acceleration
        if abs(expected_displacement) + stop_distance(ips, ipss) >= abs(inches) and do_decel:
            ips -= ipss / TICK_PER_SEC           # decel
        elif ips < target_ips:
            ips += target_ips / TICK_PER_SEC     # accel
        else:
            ips = target_ips            # cap vel at target_ips

        # Find expected position
        expected_displacement += ips / TICK_PER_SEC * dir_mod      # dir_mod adjusts for moving fwd/bwd

        # Find actual position
        displacement_l = pos_drive_l() - pos_start_l
        displacement_r = pos_drive_r() - pos_start_r

        adjustment_r = pid_drive_r.adjust(expected_displacement, displacement_r)
        adjustment_l = pid_drive_l.adjust(expected_displacement, displacement_l)
        adjustment_dir = pid_dir.adjust(all_globals.target_heading, imu_rotation)

        vel_rpm = ips / DRIVE_REV_TO_IN * 60
        
        drive_r.spin(vex.FORWARD, dir_mod * vel_rpm + adjustment_r - adjustment_dir, vex.RPM)
        drive_l.spin(vex.FORWARD, dir_mod * vel_rpm + adjustment_l + adjustment_dir, vex.RPM)

        vex.wait(MSEC_PER_TICK, vex.MSEC)
        
    if do_decel:
        drive_r.stop(vex.BRAKE)
        drive_l.stop(vex.BRAKE)
    else:
        drive_r.stop(vex.COAST)
        drive_l.stop(vex.COAST)

def drive_turn(degrees, outer_radius, target_ips, ipss, reversed):
    # Loop vex.wait times
    TICK_PER_SEC = 50
    MSEC_PER_TICK = 20

    # PID constants
    DRIVE_KP = 0.005   
    DRIVE_KI = 0.00   
    DRIVE_KD = 1.9

    # Update robot's target heading
    all_globals.inc_target_heading(degrees)

    pid_drive_r = Pid(DRIVE_KP, DRIVE_KI, DRIVE_KD)
    pid_drive_l = Pid(DRIVE_KP, DRIVE_KI, DRIVE_KD)
    
    ips = 0
    outer_displacement = 0
    pos_start_r = pos_drive_r()
    pos_start_l = pos_drive_l()

    # radius of turn
    inner_radius = outer_radius - all_globals.wheel_to_wheel_dist
    radius_ratio = inner_radius / outer_radius

    dir_mod = 1 if degrees > 0 else -1

    while ips >= 0:
        # Find distance travelled since function call
        displacement_r = pos_drive_r() - pos_start_r
        displacement_l = pos_drive_l() - pos_start_l

        # Degrees remaining to complete turn
        degrees_remaining = all_globals.target_heading - imu_rotation()

        # Handle acceleration
        # radians remaining * inches per radian; in other words, inches remaining
        if abs(degrees_remaining / RAD_TO_DEG * outer_radius) - stop_distance(ips, ipss) <= 0:
            ips -= ipss / TICK_PER_SEC      # decel
        elif ips < target_ips:
            ips += ipss / TICK_PER_SEC      # accel
        else:
            ips = target_ips                # cap at target_ips

        # Convert ips to rpm
        outer_vel_rpm = ips / DRIVE_REV_TO_IN * 60 * (-1 if reversed else 1)
        inner_vel_rpm = outer_vel_rpm * radius_ratio * (-1 if reversed else 1)

        outer_displacement += ips / TICK_PER_SEC
        inner_displacement = outer_displacement * radius_ratio

        # Get PID adjustments; move the drive
        if (reversed and degrees > 0) or ((not reversed) and (not degrees > 0)):        # left is inner side
            adjustment_r = pid_drive_r.adjust(outer_displacement, displacement_r)
            adjustment_l = -1 * pid_drive_l.adjust(inner_displacement, displacement_l)

            drive_r.spin(vex.FORWARD, outer_vel_rpm + adjustment_r, vex.RPM)
            drive_l.spin(vex.FORWARD, inner_vel_rpm + adjustment_l, vex.RPM)
        else:                                                                           # right is inner side
            adjustment_r = -1 * pid_drive_r.adjust(inner_displacement, displacement_r)
            adjustment_l = pid_drive_l.adjust(outer_displacement, displacement_l)

            drive_r.spin(vex.FORWARD, outer_vel_rpm + adjustment_r, vex.RPM)
            drive_l.spin(vex.FORWARD, inner_vel_rpm + adjustment_l, vex.RPM)

        # Exit loop if we're past the desired angle
        if degrees_remaining * dir_mod < 0:
            break

        vex.wait(MSEC_PER_TICK, vex.MSEC)
    drive_r.stop(vex.BRAKE)
    drive_l.stop(vex.BRAKE)

# slightly better drive_straight, in theory
# broken right now
def drive_linear(inches, max_ips, ipss, do_decel = True):
    # Loop vex.wait times
    TICKS_PER_SEC = 50
    MSEC_PER_TICK = 20

    # PID constants
    DRIVE_KP = 0.005
    DRIVE_KI = 0
    DRIVE_KD = 1.9

    pid_drive_r = Pid(DRIVE_KP, DRIVE_KI, DRIVE_KD)
    pid_drive_l = Pid(DRIVE_KP, DRIVE_KI, DRIVE_KD)
    pid_dir = Pid(DRIVE_KP, DRIVE_KI, DRIVE_KD)     # probably should have its own kP, kI, and kD values

    # Start positions
    start_pos_r = pos_drive_r()
    start_pos_l = pos_drive_l()
    displacement_r = pos_drive_r() - start_pos_r
    displacement_l = pos_drive_l() - start_pos_l
    avg_displacement = (displacement_l + displacement_r) / 2.0

    # Setting initial velocities to allow for function chains
    target_vel_r = vel_drive_r()
    target_vel_l = vel_drive_l()

    # adjusts velocity for postive/negative distances
    dir_mod = 1 if inches > 0 else -1

    while abs(avg_displacement) < abs(inches):
        # Update distance travelled since function call
        displacement_r = pos_drive_r() - start_pos_r
        displacement_l = pos_drive_l() - start_pos_l
        avg_displacement = (displacement_r + displacement_l) / 2.0

        # Handle acceleration
        target_vel_r = handle_acceleration(displacement_r, inches, target_vel_r, max_ips, ipss, TICKS_PER_SEC, do_decel)
        target_vel_l = handle_acceleration(displacement_l, inches, target_vel_l, max_ips, ipss, TICKS_PER_SEC, do_decel)

        # Get PID adjustments
        adjustment_r = pid_drive_r.adjust(target_vel_r, vel_drive_r())
        adjustment_l = pid_drive_l.adjust(target_vel_l, vel_drive_l())
        adjustment_dir = pid_dir.adjust(all_globals.target_heading, imu_rotation())

        # Convert ips to rpm
        r_vel_rpm = target_vel_r / DRIVE_REV_TO_IN  * 60
        l_vel_rpm = target_vel_l / DRIVE_REV_TO_IN  * 60

        # Move drive
        drive_r.spin(vex.FORWARD, dir_mod * r_vel_rpm + adjustment_r + adjustment_dir, vex.RPM)
        drive_l.spin(vex.FORWARD, dir_mod * l_vel_rpm + adjustment_l + adjustment_dir, vex.RPM)

        vex.wait(MSEC_PER_TICK, vex.MSEC)

    if do_decel:
        drive_r.stop(vex.BRAKE)
        drive_l.stop(vex.BRAKE)
    else:
        drive_r.stop(vex.COAST)
        drive_l.stop(vex.COAST)

# *Much* faster drive_turn(), but less control over speed, etc.
# Doesn't work well if arcing on full omni drives
# Slightly broken; can only turn in place (if radius_ratio = 1)
def turn_pid(degrees, radius_ratio, direction):
    MSEC_PER_TICK = 20

    TURN_KP = 1.05
    TURN_KI = 0
    TURN_KD = 4.575
    # Update robot's target heading
    all_globals.inc_target_heading(degrees)

    # Create PID object
    drive_pid = Pid(TURN_KP, TURN_KI, TURN_KD)

    # Track the amount of time the robot has been within a certain value
    time_still = 0
    while (time_still < 80):
        if within_range(imu_rotation(), all_globals.target_heading, 3):
            time_still += 20
        else:
            time_still = 0

        # Find new speed of drive
        speed_r = drive_pid.adjust(all_globals.target_heading, imu_rotation()) * direction
        speed_l = speed_r * radius_ratio

        if speed_l > 100 * abs(radius_ratio):
            speed_l = 100 * abs(radius_ratio)
        elif speed_l < -100 * abs(radius_ratio):
            speed_l = -100 * abs(radius_ratio)
        if speed_r > 100 * abs(radius_ratio):
            speed_r = 100 * abs(radius_ratio)
        elif speed_r < -100 * abs(radius_ratio):
            speed_r = -100 * abs(radius_ratio)

        drive_r.spin(vex.FORWARD, speed_l, vex.PERCENT)
        drive_r.spin(vex.FORWARD, speed_l, vex.PERCENT)
        vex.wait(MSEC_PER_TICK, vex.MSEC)

# Same idea as turn_pid(), but for drive_straight()
def straight_pid(dist):
    print("WIP")
