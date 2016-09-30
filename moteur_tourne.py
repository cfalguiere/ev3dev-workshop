import ev3dev.ev3 as ev3
import time

mg = ev3.LargeMotor('outB')
md = ev3.LargeMotor('outC')
mg.run_timed(duty_cycle_sp=-75, time_sp=500)
md.run_timed(duty_cycle_sp=+75, time_sp=500)
time.sleep(3)
mg.stop()
md.stop()

quit()

