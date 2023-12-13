import time
import datetime
start_time=round(time.time(),2)
#Startknopf gedrückt
state = bool(input("Taster gedrückt? "))
if (state):
    state = False
    while (state ==False): #bis wieder auf true wiederholen
        Lampe = True #Lampe würde angehen
        time.sleep(3) #3s Lampe an
        Lampe = False
        time.sleep(3)
        #Lampe blinkt im 3s takt

        #wenn der Blinkvorgang länger als 20s andauert, stoppt das blinken und lampe geht aus
        if (time.time()-start_time > 20): 
            state = True
            print("Länger als 20 sekunden an")
end_time=round(time.time(),2)
laufzeit=end_time-start_time
print("das Programm lief %s Sekunden" % laufzeit)

