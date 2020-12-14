#!/usr/bin/env python3

import os
import sys
import time
import pyfiglet
import subprocess
import shlex

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
	logo = pyfiglet.figlet_format("WifiConfusion \n", font = "slant")
	print(P, logo)
logo()
print(R,"						BY : ExpectionRegret")

from simple_term_menu import TerminalMenu

def quiter():
        quiter = pyfiglet.figlet_format("Thanks for Using \n", font = "slant")
        print(R, quiter)

def errorlog():
        if os.system('command') == 0:
            print("Interface successfully accepted and enabled monitor mode")
        else:
            print("Interface failed to accept")

def errorfake():
        if os.system('command') == 0:
            print("Generated successfully")
        else:
            print("Error")

def errorstop():
        if os.system('command') == 0:
            print("Disabled Successfully")
        else:
            print("Unable to Find Interface")

def main():
    main_menu_title = "Wifi-Confusion\n"
    main_menu_items = ["Fake AP Generator", "Quit"]
    main_menu_cursor = ">>>>"
    main_menu_cursor_style = ("fg_red", "bold")
    main_menu_style = ("bg_red", "fg_yellow")
    main_menu_exit = False

    main_menu = TerminalMenu(menu_entries=main_menu_items,
                             title=main_menu_title,
                             menu_cursor=main_menu_cursor,
                             menu_cursor_style=main_menu_cursor_style,
                             menu_highlight_style=main_menu_style,
                             cycle_cursor=True,
                             clear_screen=False)

    edit_menu_title = "Fake AP Generator\n"
    edit_menu_items = ["Nano Editior for list", "Gedit Editior for list", "Enable MonitorMode" , "Stop MonitorMode" , "Generate Fake Wifi Access Points", "Back to Main Menu"]
    edit_menu_back = True
    edit_menu = TerminalMenu(edit_menu_items,
                             edit_menu_title,
                             main_menu_cursor,
                             main_menu_cursor_style,
                             main_menu_style,
                             cycle_cursor=True,
                             clear_screen=True)

    while not main_menu_exit:

        main_sel = main_menu.show()

        if main_sel == 0:
            while not edit_menu_back:
                edit_sel = edit_menu.show()
                if edit_sel == 0:
                    logo()
                    print("Nano Editior")
                    os.system('cd src && nano wifi.lst')
                    time.sleep(1)
                elif edit_sel == 1:
                    logo()
                    print("Gedit Editior")
                    os.system('cd src && touch wifi.lst && gedit wifi.lst')
                    time.sleep(2)
                elif edit_sel == 2:
                    logo()
                    print("Enable Montior Mode By Entering Your interface")
                    interface = input("Enter the interface name: ")
                    command = "airmon-ng start %s"%(interface)
                    errorlog()
                    subprocess.check_call(shlex.split(command),stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
                    time.sleep(5)
                elif edit_sel == 3:
                      logo()
                      print("Disabling Monitor Mode")
                      stop = input("Enter the interface name: ")
                      command = "airmon-ng stop %s"%(stop)
                      errorstop()
                      subprocess.check_call(shlex.split(command),stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
                elif edit_sel == 4:
                      logo()
                      print("Generator of FAKE AP's")
                      print("Note:In Case To Stop The Process Hit CRTL+C or CTRL+Z")
                      monitor_mode = input("Enter monitor mode interface: ")
                      wifi_lst = input("Enter path of the wifi.lst: ")
                      command = "mdk3 %s b -c 1 -f %s"%(monitor_mode,wifi_lst)
                      errorfake()
                      subprocess.check_call(shlex.split(command),stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL)
                      time.sleep(5)
                elif edit_sel == 5:
                    edit_menu_back = True
            edit_menu_back = False
        elif main_sel == 1:
                main_menu_exit = True
                quiter()
                time.sleep(5)
if __name__ == "__main__":
    main()
