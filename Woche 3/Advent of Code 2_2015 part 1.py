import os

def einlesen(Endgerät):
    if Endgerät != 'ja':
        path = 'D:\DHBW\Programmieren\Repo\Programmieren\Woche 3\\2_2015.txt'
    else:
        path = 'C:\\Users\\jonin\\Documents\\Programmieren\\Programmieren Repo\\Weekly\\Programmieren\\Woche 3\\2_2015.txt'
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
        lw=w*l*w
        wh=2*w*h
        lh=2*l*h
        kleinster = min(lw,wh,lh)
        flaeche =2*l*w+2*w*h+2*h*l
        Gesamtfläche += flaeche + kleinster
    
    return Gesamtfläche
            
        
konsole = input("Bist du am Laptop? ").lower       
print(berechnung(einlesen(konsole)))