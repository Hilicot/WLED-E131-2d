from time import sleep
import numpy as np
from wled_e131_2d.RGB_effects.RGBEffectBase import RGBEffectBase


class RGBWipe(RGBEffectBase):

    def generate_frame(self, frame_number: int) -> np.ndarray:
        sleep(0.1)
        frame = np.zeros((self.device.num_leds, 3))
        frame[:frame_number, 0] = 1
        return frame
