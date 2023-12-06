import time
laenge= int(input("Länge des Countdowns in Sekunden: "))
button=bool(input("Countdown starten? "))
if button == True:
   for i in range(laenge,0,-1):
      print(i)
      time.sleep(1)
   time.sleep(1)
   print("Start!!!")
else:
   print("Warten auf Start des Countdowns")
