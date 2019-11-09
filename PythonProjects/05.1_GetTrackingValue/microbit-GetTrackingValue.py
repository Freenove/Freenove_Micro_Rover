from microbit import *
while True:
    sensor_value=pin14.read_digital()<<2|pin15.read_digital()<<1|pin16.read_digital()
    display.show(sensor_value)