import ev3dev.ev3 as ev3

mg = ev3.LargeMotor('outB')
mg.run_timed(time_sp=3000, duty_cycle_sp=75)

quit()

