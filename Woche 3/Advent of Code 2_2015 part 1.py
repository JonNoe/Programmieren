import os

def einlesen(Endgerät):
    if Endgerät == "ja":
        path = 'C:\\Users\\jonin\\Documents\\Programmieren\\Programmieren Repo\\Weekly\\Programmieren\\Woche 3\\2_2015.txt'
    else:
         path = 'D:\DHBW\Programmieren\Repo\Programmieren\Woche 3\\2_2015.txt'
    try:
        with open(path,'r') as file:
            werte = file.readlines()
    except FileNotFoundError:
        print(f"Datei {path} nicht gefunden")
    return(werte)


def berechnung(lxwxh):
    Gesamtfläche = 0
    for i in range (len(einlesen(konsole))):
        lxwxh[i]=lxwxh[i].strip('\n')
        l, w, h =lxwxh[i].split('x')
        #Um mit den variablen rechnen zu können
        l = int(l)
        w=int(w)
        h=int(h)
        #Flächenberechnung
        lw=l*w
        wh=w*h
        lh=l*h
        kleinster = min(lw,wh,lh)
        flaeche =2*lw+2*wh+2*lh
        Gesamtfläche += flaeche + kleinster
    
    return Gesamtfläche
            
#Unterscheidung der Ablageorte zwischen meinem PC und Laptop herausfinden
konsole = input("Bist du am Laptop? ").lower() 
print(berechnung(einlesen(konsole)))