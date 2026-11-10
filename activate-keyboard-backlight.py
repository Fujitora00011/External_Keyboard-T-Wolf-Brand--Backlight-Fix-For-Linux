#!/usr/bin/env python3
from pathlib import Path

import subprocess

kb_lights = Path("/sys/class/leds/")
files = list(kb_lights.rglob("input*scrolllock/brightness"))


keyboard_cmd = input("Do you want to activate the keyboard backlight? (y/n): ")

for file in files:
    if keyboard_cmd == "y":
        subprocess.run(["sudo", "tee", str(file)], input=b"1", check=True)
    else:
        subprocess.run(["sudo", "tee", str(file)], input=b"0", check=True)