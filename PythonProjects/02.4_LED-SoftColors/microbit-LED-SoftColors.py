from Freenove_Micro_Rover import *
Rover = Micro_Rover()
while True:
    for i in range(360):
        R,G,B = Rover.hsl_to_rgb(i)
        Rover.all_led_show(255,R,G,B)
        sleep(10)