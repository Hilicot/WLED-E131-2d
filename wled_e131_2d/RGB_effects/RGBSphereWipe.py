from colorsys import hsv_to_rgb
import colorsys
from time import sleep
import numpy as np
from wled_e131_2d.RGB_effects.RGBEffectBase import RGBEffectBase
from wled_e131_2d.utils import rgb2hsv


class RGBSphereWipe(RGBEffectBase):

    def generate_frame(self, frame_number: int) -> np.ndarray:
        sleep(.01)   
        frame_number_capped = frame_number % 18
        frame = self.frame

        max_distance = np.linalg.norm(np.array([self.device.height, self.device.width]) - self.device.center)
        for i in range(self.device.height):
            for j in range(self.device.width):
                distance = np.linalg.norm(np.array([i, j]) - self.device.center)
                if distance < frame_number_capped:
                    fade_factor = (distance / frame_number)
                    hue = (distance / max_distance + frame_number / 50) % 1.0
                    rgb = np.array(colorsys.hsv_to_rgb(hue, 1, 0.1))
                    frame[i, j] = rgb 
        return frame
