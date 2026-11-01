#!/usr/bin/env python3
from pathlib import Path

import subprocess

kb_lights = Path("/sys/class/leds/")
files = list(kb_lights.rglob("input*scrolllock/brightness"))

#print(files)
#path.write_text("1")

keyboard_cmd = input("Do you want to activate the keyboard backlight? (y/n): ")

if keyboard_cmd == "y":
    for file in files:
        #print(file)
        subprocess.run(["sudo", "tee", str(file)], input=b"1", check=True)
else:
    for file in files:
        #print(file)
        subprocess.run(["sudo", "tee", str(file)], input=b"0", check=True)