import signal
import time
import numpy as np
from wled_e131_2d.Device import Device
from wled_e131_2d.E131Module import E131Module
from wled_e131_2d.RGB_effects.RGBEffectBase import RGBEffectBase
from wled_e131_2d.RGB_effects.RGBSphereWipe import RGBSphereWipe
from wled_e131_2d.RGB_effects.RGBWipe import RGBWipe

rgb_effect_func = RGBSphereWipe


def main():
    signal.signal(signal.SIGINT, termination_handler)

    device = Device(e131)
    e131.send_data(np.zeros((256,3)))

    rgb_effect = rgb_effect_func(device)
    rgb_effect.run()

    e131.close()

def termination_handler(signal, frame):
    print("Termination signal received")
    e131.close()
    exit(0)

if __name__ == "__main__":
    e131 = E131Module(led_number=256)
    e131.set_ip("192.168.1.213")
    main()