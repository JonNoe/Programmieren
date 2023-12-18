import os
import math

def einlesen():
    Eingabewerte =  "C:\\Users\\jonin\\Documents\\Programmieren\\Programmieren Repo\\Weekly\\Programmieren\\Woche 2\\input.txt"
    try:
        with open(Eingabewerte,"r") as file:
            massen = file.readlines()
    except FileNotFoundError:
        print(f"Datei {Eingabewerte} nicht gefunden")
    return(massen)


def Treibstoff(modulmassen):
    ins_Treibstoff=0
    for i in range(0,len(einlesen())):
        zeug = einlesen()
        zeug[i] = int(zeug[i].strip('\n'))
        ins_Treibstoff += int(zeug[i] / 3) - 2
   
    return(ins_Treibstoff)
        
print(f"Der Weihnachtsmann braucht {Treibstoff(einlesen)} Liter Treibstoff")

