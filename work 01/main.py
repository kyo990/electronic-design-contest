from machine import Pin
import time

DELAY = 1
PINS = (Pin(10, Pin.OUT), Pin(11, Pin.OUT), Pin(12, Pin.OUT))
SINGLE = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
BLINK_TIMES = 3
PAIRS = ((1, 1, 0), (0, 1, 1), (1, 0, 1))


def set_all(value):
    for pin in PINS:
        pin.value(value)


def show(color):
    for pin, value in zip(PINS, color):
        pin.value(value)
    time.sleep(DELAY)
    set_all(0)


while True:
    for color in SINGLE:
        show(color)

    for _ in range(BLINK_TIMES):
        set_all(1)
        time.sleep(DELAY)
        set_all(0)
        time.sleep(DELAY)

    for color in PAIRS:
        show(color)
