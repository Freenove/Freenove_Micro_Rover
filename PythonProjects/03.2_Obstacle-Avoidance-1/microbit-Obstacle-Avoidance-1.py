from Freenove_Micro_Rover import *
Rover = Micro_Rover()
while True:
    distance = Rover.get_distance()
    if distance >= 15:
        Rover.motor(100,100)
    else:
        Rover.motor(-100,100)