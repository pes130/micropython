#Pablo
import machine
import time

pin = machine.Pin(2, machine.Pin.OUT)
i=1
def toggle(p):
    p.value(not p.value())

while True:
    toggle(pin)
    print(i)
    time.sleep_ms(500)
    i=i+1

