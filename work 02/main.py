from machine import Pin
import time

T_MS = 20
N = 100
STEP_US = T_MS * 1000 // N
DUTY_STEP = 1

led = Pin(10, Pin.OUT)   # 红灯：GP10，串 220Ω


def frame(duty):
    on = duty * N // 100
    for i in range(N):
        led.value(1 if i < on else 0)
        time.sleep_us(STEP_US)


while True:
    for duty in range(0, 101, DUTY_STEP):
        frame(duty)
    for duty in range(100, -1, -DUTY_STEP):
        frame(duty)
