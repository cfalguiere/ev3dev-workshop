import ev3dev.ev3 as ev3

ts = ev3.TouchSensor()
couleurs = (ev3.Leds.GREEN, ev3.Leds.RED)

count = 0
while count < 10:
	pos = ts.value()
	ev3.Leds.set_color(ev3.Leds.LEFT, couleurs[pos])
	if pos == 1:
		count += 1
	
pos = 0
ev3.Leds.set_color(ev3.Leds.LEFT, couleurs[pos])

quit()

