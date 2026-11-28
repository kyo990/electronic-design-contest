# work3 最终实现：定时器中断 PWM + 三路彩色流转 + 串口打印
# 对应《闯关指南.md》第 1–8 关，已通过全部验收。
# 学习时请按各关自己写，写完再和这份对照，不要一开始就抄。

from machine import Pin, Timer
import time

TICK_MS = 1          # 定时器中断周期，毫秒
TICKS = 20           # 一个 PWM 周期的 tick 数（20 → 50Hz）
DUTY_STEP = 1        # duty 每次变化的百分点
BREATH_MS = 20       # 主循环每一拍停多久，毫秒
PHASE_STEP = 1       # 彩色流转的相位步进
ORANGE = (100, 30, 0)
FADE_STEP = 10       # 每 phase 淡入/淡出的亮度百分比
PRINT_MS = 2000      # 串口打印间隔，毫秒

LED_PINS = (10, 11, 12)     # GP10=红，GP11=绿，GP12=蓝
leds = [Pin(p, Pin.OUT) for p in LED_PINS]
counters = [0, 0, 0]
duty_r = duty_g = duty_b = 0


def set_duty(r, g, b):
    global duty_r, duty_g, duty_b
    duty_r, duty_g, duty_b = r, g, b


last_print = time.ticks_ms()


def beat():
    global last_print
    time.sleep_ms(BREATH_MS)
    now = time.ticks_ms()
    if time.ticks_diff(now, last_print) >= PRINT_MS:
        print("duty r/g/b =", duty_r, duty_g, duty_b)
        last_print = now


def breathe_one(k):
    color = [0, 0, 0]
    for d in range(0, 101, DUTY_STEP):
        color[k] = d
        set_duty(color[0], color[1], color[2])
        beat()
    for d in range(100, -1, -DUTY_STEP):
        color[k] = d
        set_duty(color[0], color[1], color[2])
        beat()


def on_tick(timer):
    duties = (duty_r, duty_g, duty_b)
    for k in range(3):
        counters[k] = (counters[k] + 1) % TICKS
        on = duties[k] * TICKS // 100
        leds[k].value(1 if counters[k] < on else 0)


def color_wheel():
    for phase in range(0, 100, PHASE_STEP):
        color = [0, 0, 0]
        for k in range(3):
            x = (phase + k * 33) % 100
            color[k] = 100 - abs(2 * x - 100)
        scale = min(100, phase * FADE_STEP, (99 - phase) * FADE_STEP)
        set_duty(color[0] * scale // 100, color[1] * scale // 100, color[2] * scale // 100)
        beat()


def breathe_color(color):
    for d in range(0, 101, DUTY_STEP):
        set_duty(color[0] * d // 100, color[1] * d // 100, color[2] * d // 100)
        beat()
    for d in range(100, -1, -DUTY_STEP):
        set_duty(color[0] * d // 100, color[1] * d // 100, color[2] * d // 100)
        beat()


timer = Timer()
timer.init(period=TICK_MS, mode=Timer.PERIODIC, callback=on_tick)

while True:
    for k in range(3):
        breathe_one(k)
    color_wheel()
    breathe_color(ORANGE)
