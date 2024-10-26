import numpy as np
from wled_e131_2d import E131Module


class Device:
    def __init__(self, e131: E131Module):
        self.num_leds = 256
        self.e131 = e131
        self.width = 32
        self.height = 8

    @property
    def center(self):
        return (self.height//2, self.width//2)
    
    @property
    def clean_strip(self):
        return np.zeros((self.num_leds,3))
    
    @property
    def clean_matrix(self):
        return np.zeros((self.height, self.width, 3))
    
    @property
    def matrix_positions(self):
        return np.array(np.meshgrid(range(self.width), range(self.height))).T.reshape(-1, 2)

