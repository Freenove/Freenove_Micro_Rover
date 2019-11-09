from Freenove_Micro_Rover import *
Rover = Micro_Rover()
while True:
  distance = Rover.get_distance()
  display.scroll(distance)