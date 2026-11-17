# work2 起点：软件 PWM 呼吸灯
# 本文件只完成第 1 关的闪烁基线，用来确认红灯确实接在 GP10。
# 请按《闯关指南.md》逐关实现 PWM，不要直接抄成品。

from machine import Pin
import time

led = Pin(10, Pin.OUT)   # 红灯：GP10，串 220Ω

while True:
    led.value(1)
    time.sleep_ms(500)
    led.value(0)
    time.sleep_ms(500)
