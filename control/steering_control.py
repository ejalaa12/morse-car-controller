from math import pi
from utils import wrap_radians

class SteeringController:
    def __init__(self, state, controls):
        self.vstate = state
        self.controls = controls
        self.enabled = False
        self.target_heading = 0
        self.last_heading = 0
        self.Kp = 1.0
        self.last_heading_error = 0   

    def set_steer(self, steering):
        self.enabled = False
        self.controls.set_steer(steering)

    def set_heading(self, heading):
        #self.enabled = True
        self.target_heading = heading

    def update_heading(self):
        if not self.enabled:
            return

        heading = self.vstate.yaw
        self.last_heading_error = wrap_radians(self.target_heading - heading)
        self.controls.set_steer(self.Kp*self.last_heading_error)
    
    def status(self):
        d = {}
        d['enabled'] = self.enabled
        d['target_heading'] = self.target_heading
        d['heading_error'] = self.last_heading_error
        return d
