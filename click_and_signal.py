import pyautogui
from configparser import ConfigParser
import os
import time

config = ConfigParser()
config.read("C:/path/to/config.txt")

iso = config.getint("Camera", "iso_value")
shutter_speed = config.get("Camera", "shutter_speed")
aperture_value = config.getfloat("Camera", "aperture_value")

base = "chaarAdhyay"

for idx in range(1):
    dest = f"{base}/{idx}"
    if not os.path.exists(f"C:/{dest}"):
        os.makedirs(f"C:/{dest}")

    for y in [250, 300, 350, 400]:
        pyautogui.moveTo(100, y)
        pyautogui.click()
        time.sleep(1)

        # Write simple relative signal
        with open("C:/capture_signal.txt", "w") as f:
            f.write(f"{y},{dest},{iso},{shutter_speed},{aperture_value}\n")

        while os.path.exists("C:/capture_signal.txt"):
            time.sleep(0.5)
