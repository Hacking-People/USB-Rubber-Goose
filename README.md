# USB-Rubber-Goose
An affordable and easy take on the infamous USB Rubber Ducky by Hak5

It is a python driven version,
It takes commands from a commands.txt file and executes them.


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
