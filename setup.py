#!/usr/bin/env python3

import os
import sys
import time
import pyfiglet

# Console Colors
W  = '\033[0m\033[1m'  # white (normal)
R  = '\033[1m\033[31m' # red
G  = '\033[1m\033[32m' # green
O  = '\033[1m\033[33m' # orange
B  = '\033[1m\033[34m' # blue
P  = '\033[1m\033[35m' # purple
C  = '\033[1m\033[36m' # cyan
GR = '\033[1m\033[37m' # gray
T  = '\033[1m\033[93m' # tan

os.system('clear');

def logo():
        logo = pyfiglet.figlet_format("SETUP \n", font = "slant")
        print(R, logo)
logo()
print(R,"                                               FOR Wifi-Confusion")

os.system('pip3 install -r requirements.txt && apt install python3 mdk3 aircrack-ng')

def setup():
        setup = pyfiglet.figlet_format("SETUP \n", font = "slant")
        print(O, setup)
setup()
print(R,"Successfully setup completed")
time.sleep(3)
os.system('clear')

