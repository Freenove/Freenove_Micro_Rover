from Freenove_Micro_Rover import *
Rover = Micro_Rover()
while True:
    distance = Rover.get_distance()
    R,G,B = Rover.hsl_to_rgb(Rover.constrain(distance,0,240))
    Rover.all_led_show(255,R,G,B)
    if distance >= 15:
        Rover.motor(100,100)
    else:
        Rover.motor(-100,100)