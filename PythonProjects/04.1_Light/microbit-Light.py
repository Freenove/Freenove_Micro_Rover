from microbit import *
while True:
   value = pin1.read_analog()
   display.scroll(value)