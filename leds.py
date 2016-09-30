import ev3dev.ev3 as ev3
import time

ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
time.sleep(2)
ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.YELLOW)
time.sleep(2)
ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
time.sleep(2)

quit()

