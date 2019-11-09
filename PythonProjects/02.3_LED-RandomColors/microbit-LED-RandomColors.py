import random
from Freenove_Micro_Rover import *
Rover = Micro_Rover()
while True:
    R=random.randint(0,255)
    G=random.randint(0,255)
    B=random.randint(0,255)
    Rover.all_led_show(255,R,G,B)
    sleep(200)