import os

def einlesen():
    path = 'C:\\Users\\jonin\\Documents\\Programmieren\\Programmieren Repo\\Weekly\\Programmieren\\Woche 3\\2_2015.txt'
    try:
        with open(path,'r') as file:
            werte = file.readlines()
    except FileNotFoundError:
        print(f"Datei {path} nicht gefunden")
    return(werte)

def berechnung(lxbxh):
    for i in range (len(einlesen())):
        lxbxh[i]=lxbxh[i].str
print(einlesen())