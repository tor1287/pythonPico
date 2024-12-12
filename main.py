from machine import Pin, Timer

led = Pin(3, mode=Pin.OUT) #specified argument from doc.micropython
tim = Timer()
def tick(timer):
    global led
    led.toggle()

tim.init(freq= 2, mode=Timer.PERIODIC, callback=tick)