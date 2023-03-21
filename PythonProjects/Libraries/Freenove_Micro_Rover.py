from microbit import *
import math,ustruct
from time import sleep_us,ticks_us
import machine
class Micro_Rover(object):
    lastEchoDuration = 0
    def __init__(self):
        self.add = 0x43
        i2c.write(self.add, bytearray([0x00, 0x00]), repeat=False)
        self.set_all_pwm(0, 0)
        i2c.write(self.add, bytearray([0x01, 0x04]), repeat=False)
        i2c.write(self.add, bytearray([0x00, 0x01]), repeat=False)
        sleep(5)
        i2c.write(self.add, bytearray([0x00]), repeat=False)
        mode1s = i2c.read(self.add, 1)
        # mode1 = ustruct.unpack('<H', mode1)[0]
        mode1 = mode1s[0]
        mode1 = mode1 & ~0x10
        i2c.write(self.add, bytearray([0x00, mode1]), repeat=False)
        sleep(5)
    def set_pwm(self, channel, on, off):
        if on is None or off is None:
            i2c.writ(self.add, bytearray([0x06+4*channel]), repeat=False)
            data = i2c.read(self.add, 4)
            return ustruct.unpack('<HH', data)
        i2c.write(self.add, bytearray([0x06+4*channel, on & 0xFF]), repeat=False)
        i2c.write(self.add, bytearray([0x07+4*channel, on >> 8]), repeat=False)
        i2c.write(self.add, bytearray([0x08+4*channel, off & 0xFF]), repeat=False)
        i2c.write(self.add, bytearray([0x09+4*channel, off >> 8]), repeat=False)
    def set_all_pwm(self, on, off):
        i2c.write(self.add, bytearray([0xFA, on & 0xFF]), repeat=False)
        i2c.write(self.add, bytearray([0xFB, on >> 8]), repeat=False)
        i2c.write(self.add, bytearray([0xFC, off & 0xFF]), repeat=False)
        i2c.write(self.add, bytearray([0xFD, off >> 8]), repeat=False)
    def map(self,value,fromLow,fromHigh,toLow,toHigh):
        return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow
    def constrain(self,Value,Low,High):
        if Value <= Low:
            return Low
        elif Value >= High:
            return High
        else:
            return Value
    def all_led_show(self,brightness,R,G,B):
        b=brightness/255
        R=int((R/255)*4095*b)
        G=int((G/255)*4095*b)
        B=int((B/255)*4095*b)
        for i in range(4):
            self.set_pwm(5+3*i,0,R)
            self.set_pwm(6+3*i,0,G)
            self.set_pwm(4+3*i,0,B)
    def led_show(self,index,brightness,R,G,B):
        b=brightness/255
        R=int((R/255)*4095*b)
        G=int((G/255)*4095*b)
        B=int((B/255)*4095*b)
        for i in range(4):
            if index>>i & 0x01:
                if i==0:
                    self.set_pwm(14,0,R)
                    self.set_pwm(15,0,G)
                    self.set_pwm(13,0,B)
                else:
                    self.set_pwm(5+3*(i-1),0,R)
                    self.set_pwm(6+3*(i-1),0,G)
                    self.set_pwm(4+3*(i-1),0,B)
    def hsl_to_rgb(self,degree):
        degree=degree/360*255
        if degree < 85:
            red = 255 - degree * 3
            green = degree * 3
            blue = 0
        elif degree < 170:
            degree = degree - 85
            red = 0
            green = 255 - degree * 3
            blue = degree * 3
        else:
            degree = degree - 170
            red = degree * 3
            green = 0
            blue = 255 - degree * 3
        return int(red),int(green),int(blue)
    def motor(self,left,right):
        left=int(self.map(left,-255,255,-4095,4095))
        right=int(self.map(right,-255,255,-4095,4095))
        if left > 0:
            self.set_pwm(0,0,left)
            self.set_pwm(1,0,0)
        elif left < 0:
            self.set_pwm(0,0,0)
            self.set_pwm(1,0,abs(left))
        else:
            self.set_pwm(0,0,0)
            self.set_pwm(1,0,0)
        if right > 0:
            self.set_pwm(2,0,right)
            self.set_pwm(3,0,0)
        elif right < 0:
            self.set_pwm(2,0,0)
            self.set_pwm(3,0,abs(right))
        else:
            self.set_pwm(2,0,0)
            self.set_pwm(3,0,0)
    def get_distance(self):
        pin12.write_digital(0)
        sleep_us(2)
        pin12.write_digital(1)
        sleep_us(15)
        pin12.write_digital(0)

        v = pin13.read_digital() # for micro bit v1.5, may need to set Pin13 as the input mode.
        t = machine.time_pulse_us(pin13,1,35000)
        if (t <= 0 and self.lastEchoDuration >= 0) :
            t = self.lastEchoDuration

        self.lastEchoDuration = t
        return round(t * 0.017)
