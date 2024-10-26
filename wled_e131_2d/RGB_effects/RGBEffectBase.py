from abc import ABC, abstractmethod
from time import sleep
import numpy as np

from wled_e131_2d import Device

class RGBEffectBase:
    def __init__(self, device: Device):
        self.device = device
        self.frame = device.clean_matrix

    def run(self):
        frame_number = 0
        while True:
            frame = self.generate_frame(frame_number)
            self.device.e131.send_data(frame*255)
            frame_number += 1

 
    def generate_frame(self, frame_number: int) -> np.ndarray:
        pass
