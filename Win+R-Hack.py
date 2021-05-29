import time #for waiting
import digitalio #for interfacing with pins
import board #for interfacing with pins

import usb_hid #to get usb interface devices
from adafruit_hid.keyboard import Keyboard #be able to send key presses
from adafruit_hid.keycode import Keycode #be able to send keycodes
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS #be able to type

keyboard = Keyboard(usb_hid.devices) #set up the usb hid device
layout = KeyboardLayoutUS(keyboard) #setup the keyboard interface


def windowsRun(text):
    keyboard.send(Keycode.WINDOWS, Keycode.R) #press Win+R keys
    time.sleep(1) #wait 1 second for the run box to open
    layout.write(f"{text}\n") #type the text

time.sleep(3)
windowsRun('notepad')