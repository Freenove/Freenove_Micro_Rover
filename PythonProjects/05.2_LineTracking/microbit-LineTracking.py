from Freenove_Micro_Rover import *
Rover = Micro_Rover()
display.show(Image.HAPPY)
while True:
    sensor_value=pin14.read_digital()<<2|pin15.read_digital()<<1|pin16.read_digital()
    if sensor_value==2 or sensor_value==5:
        Rover.all_led_show(255,0,255,0)
        Rover.motor(110,110)
    elif sensor_value==4 or sensor_value==6:
        Rover.all_led_show(255,255,0,0)
        Rover.motor(25,110)
    elif sensor_value==1 or sensor_value==3:
        Rover.all_led_show(255,0,0,255)
        Rover.motor(110,25)
    else:
        Rover.all_led_show(255,255,0,255)
        Rover.motor(0,0)