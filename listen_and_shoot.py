import time
import os
from camera import take_picture

signal_path = "/mnt/c/capture_signal.txt"

while True:
    if os.path.exists(signal_path):
        with open(signal_path, "r") as f:
            line = f.readline().strip()
            y, dest, iso, shutter_speed, aperture = line.split(",")

        print(f"📸 Shooting {y}.jpg in {dest}")
        take_picture(y, dest, int(iso), shutter_speed, float(aperture))

        os.remove(signal_path)
    time.sleep(1)
