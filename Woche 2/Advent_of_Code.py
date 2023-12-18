import os
import math

def einlesen():
    Eingabewerte =  "C:\\Users\\jonin\\Documents\\Programmieren\\Programmieren Repo\\Weekly\\Programmieren\\Woche 2\\input.txt"
    try:
        with open(Eingabewerte,"r") as file:
            massen = file.read()
    except FileNotFoundError:
        print(f"Datei {Eingabewerte} nicht gefunden")
    return(massen)


def Treibstoff(modulmassen):
    ins_Treibstoff=0
    for masse in range(0,len(einlesen())):
        Treibstoff_pro_modul = math.floor(masse / 3)
        ins_Treibstoff = ins_Treibstoff+Treibstoff_pro_modul
    print(ins_Treibstoff)
    return(ins_Treibstoff)
        
Treibstoff(einlesen)
