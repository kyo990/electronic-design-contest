# work3 起点：第 1 关，用 Timer 让红灯定时闪烁
# 请按《闯关指南.md》逐关替换成自己的代码，不要直接抄成品。
#
# 本文件只演示“回调在中断里被自动调用”：
# 主循环什么都不做，灯照样闪，因为闪灭是定时器干的。

from machine import Pin, Timer

BLINK_MS = 500

led = Pin(10, Pin.OUT)   # 红灯：GP10，串 220Ω
state = 0


def toggle(timer):
    global state
    state = 1 - state
    led.value(state)


timer = Timer()
timer.init(period=BLINK_MS, mode=Timer.PERIODIC, callback=toggle)

while True:
    pass
