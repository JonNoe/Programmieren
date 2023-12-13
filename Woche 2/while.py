import time
import datetime
start_time=time.time()
state = bool(input("Taster gedrückt? "))
if (state):
    state = False
    while (state ==False):
        Lampe = True
        time.sleep(5)
        if (time.time() > 10):
            state = True
            print("Länger als 10 sekunden an")
print("Start des Programms: %s" % datetime.now())
print("Ende des Programms: %s" % datetime.now()+time.time())