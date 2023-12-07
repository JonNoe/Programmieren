from datetime import datetime
from datetime import date

#Definition der globalen Variable des heutigen Datums
Datum_heute = datetime.now()

def Feiertage():
    #Definition einiger Feiertage
    Nicolaus= date(year=Datum_heute.year, month=12, day=6)
    Weihnachten= date(year=Datum_heute.year, month=12, day=25)
    Feiertag = [Nicolaus,Weihnachten]
    #Gibt die Liste an Feiertagen zurück
    return Feiertag
Heute = date(year = Datum_heute.year, month=Datum_heute.month, day=Datum_heute.day)
Feiertage()

#Ausgabe des Heutigen Tages
print("Heute ist der" ,Datum_heute.day, ".",Datum_heute.month , "im Jahr" , Datum_heute.year)

#Kontrolle ob heute ein Feiertag ist
if Heute in Feiertage():
    print("Heute ist ein Feiertag")
else:
    print("Heute ist ein normaler Tag")
    print(Feiertage)

