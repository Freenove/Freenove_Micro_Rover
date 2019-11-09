from Freenove_Micro_Rover import *
Rover = Micro_Rover()
sumValue=0
for i in range(10):
    sumValue += pin1.read_analog()
centerValue=round(sumValue/10)
display.show(Image.HAPPY)
while True:
    LightingValue=pin1.read_analog()
    R,G,B=Rover.hsl_to_rgb(Rover.map(LightingValue,0,1023,0,360))
    Rover.all_led_show(255,R,G,B)
    difValue=LightingValue-centerValue
    if difValue > 20:
        Rover.motor(150,0)
    elif difValue < -20:
        Rover.motor(0,150)
    else:
        Rover.motor(100,100)