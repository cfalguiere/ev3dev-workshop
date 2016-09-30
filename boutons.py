import ev3dev.ev3 as ev3
import time

son = 'sounds/eight-bit Atari SFX-006.wav'
btn = ev3.Button()

while not btn.any():
	time.sleep(1)

ev3.Sound.play(son).wait()

quit()

