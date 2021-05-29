# USB-Rubber-Goose
An affordable and easy take on the infamous USB Rubber Ducky by Hak5

It is a python driven version,
It takes commands from a commands.txt file and executes them.

<hr>

## To Use:
- Hold down the `bootsel` button and plug in your Pico (to a computer) - this will then show as a USB storage device, 
- Copy the `.uf2` file onto the USB device(called: `RPI-RP2`) device. It should unmount itself,
- Then go into your ide [(I recommend thonny)](https://www.raspberrypi.org/documentation/pico/getting-started/)
- Then open the .py files, and save them to the board.
- ***OPTIONAL*** - If you want you can rename the `USB-Rubber-Goose.py` to `code.py` to make it run on boot,
- Now you have the USB-Rubber-Goose Code.

<hr>

## [TODO](TODO)

<hr>

### Commands:

```

write(text)
#this will output a string/ line of text that will be typed by the keyboard.

_char_to_keycode(char)
#this will return the keycode for the given key

keycode(char)
#this will press the key coresponding to the given keycode
#to see the keycodes go here: 
```
### [keycodes](keycodes) 

<hr>

### Examples:
```

write("Some text that the keyboard will type")
#output: Some text that the keyboard will type

_char_to_keycode(A)
#output: b"\x84"
#(Shift+A)

keycodes(b"\x28")
#output: \n 
#(newline/enter)

```
