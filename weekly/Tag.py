from datetime import datetime
from datetime import date

Datum = datetime.now()
def Feiertage():
    #Definition einiger Feiertage
    Nicolaus= date(year=Datum.year, month=12, day=6)
    Weihnachten= date(year=Datum.year, month=12, day=25)
    Feiertag = [Nicolaus,Weihnachten]
    #Gibt die Liste an Feiertagen zurück
    return Feiertag
Heute = date(year = Datum.year, month=Datum.month, day=Datum.day)
Feiertage()

Datum =   datetime.now()
print("Heute ist der" ,Datum.day, ".",Datum.month , "im Jahr" , Datum.year)
if Heute in Feiertage():
    print("Heute ist ein Feiertag")
else:
    print("Heute ist ein normaler Tag")
    print(Feiertage)

