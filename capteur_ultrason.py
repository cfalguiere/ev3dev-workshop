import ev3dev.ev3 as ev3

uss = ev3.UltrasonicSensor(); assert uss.connected

while True:
	distance = uss.value()
	if distance < 150:
		ev3.Sound.tone([(888, 40, 40)]).wait()
	else:
		if distance < 300:
			ev3.Sound.tone([(444, 100, 100)]).wait()
	
quit()

