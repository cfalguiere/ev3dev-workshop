import ev3dev.ev3 as ev3

gs = ev3.GyroSensor();
assert gs.connected
gs.mode = gs.MODE_GYRO_ANG

angle_initial = gs.value()

while True:
	diff_angle = gs.value() - angle_initial
	if diff_angle > 0: 
		ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
		ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
	else:
		if diff_angle < 0: 
			ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
			ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)
		else:
			ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
			ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
			

ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)

quit()

