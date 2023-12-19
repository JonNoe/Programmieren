import os
import math

def einlesen():
    Eingabewerte =  "C:\\Users\\jonin\\Documents\\Programmieren\\Programmieren Repo\\Weekly\\Programmieren\\Woche 3\\1_2015.txt"
    try:
        with open(Eingabewerte,"r") as file:
            stufen = file.read()
    except FileNotFoundError:
        print(f"Datei {Eingabewerte} nicht gefunden")
    #print(stufen)
    return(stufen)

def floor_berechnung(Stockwerke_zahl):
    #einfache Berechnung von aktuellem Stock
    hoch=Stockwerke_zahl.count('(')
    runter=Stockwerke_zahl.count(')')
    aktueller_Stock=hoch-runter
    return(aktueller_Stock)

def Keller(Stockwerke_zahl):
    aktueller_Stock=0
    anzahl_wechsel=len(einlesen())
    ist_keller = False
    for i in range(0, anzahl_wechsel & ist_keller ==True ):
        if Stockwerke_zahl[i] == '(':
            aktueller_Stock += 1
        else:
            aktueller_Stock -= 1
        if aktueller_Stock ==-1:
            print(i+1)
            ist_keller = True
    print(aktueller_Stock)
    print(anzahl_wechsel)
    
    

print(f"Der Weihnachtsmann befindet sich auf dem {floor_berechnung(einlesen())}. Stock")
Keller(einlesen())