import vex
from robot_config import *

class Pid:
    def __init__(self, init_kp, init_ki, init_kd):
        self.kp = init_kp
        self.ki = init_ki
        self.kd = init_kd

        self.error = 0
        self.sum = 0
        self.prev_error = 0
        self.deriv = 0

    def tune_kp(self, value, mod):
        self.kp += value * mod
        print("kp: " + self.kp + "")
        brain.screen.set_cursor(3, 4)
        brain.screen.print("kp: " + self.kp + "")

    def tune_ki(self, value, mod):
        self.ki += value * mod
        print("ki: " + self.ki + "")
        brain.screen.set_cursor(5, 4)
        brain.screen.print("ki: " + self.ki + "")

    def tune_kd(self, value, mod):
        self.kd += value * mod
        print("kd: " + self.kd + "")
        brain.screen.set_cursor(7, 4)
        brain.screen.print("kd: " + self.kd + "")

    def adjust(self, setpoint, sensor_value):
        self.error = setpoint - sensor_value
        # Only incrememnt sum if the i loop is used
        if not self.ki == 0:
            self.sum += self.error
        self.deriv = self.error - self.prev_error
        self.prev_error = self.error

        p_term = self.error * self.kp
        i_term = self.sum * self.ki
        d_term = self.deriv * self.kd

        return p_term + i_term + d_term
