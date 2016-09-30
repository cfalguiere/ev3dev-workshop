import ev3dev.ev3 as ev3
import time

mg = ev3.LargeMotor('outB')
md = ev3.LargeMotor('outC')
mg.run_forever()
md.run_forever()
time.sleep(3)
mg.stop()
md.stop()

quit()

