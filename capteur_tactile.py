import ev3dev.ev3 as ev3

ts = ev3.TouchSensor()
est_fini = ts.value()
while not est_fini:
	est_fini = ts.value()
	
print 'Yessss!'

quit()

