import os

def einlesen():
    Eingabewerte =  "C:\\Users\\jonin\\Documents\\Programmieren\\Programmieren Repo\\Weekly\\Programmieren\\Woche 3\\3_2015.txt"
    try:
        with open(Eingabewerte,"r") as file:
            directions = file.read()
    except FileNotFoundError:
        print(f"Datei {Eingabewerte} nicht gefunden")
    #print(stufen)
    return(directions)

def Ortsberechnung(directions):
    Ort_jetzt=[(0,0)] #Liste in Liste , da man beide variablen überschreiben will hier: links x rechts y
    richtungswechsel = len(directions)

    for i in range(richtungswechsel):
        letzter_Wert = Ort_jetzt[-1] #Kopiert den Endwert des letzten Durchgangs wie ein Speicher
        if (directions[i]=='>'):
            Ort_jetzt.append((letzter_Wert[0]+1, letzter_Wert[1])) #hier x wert des letzten durchgangs +1 (letzter_Wert[0] ist der linke Wert von ort_jetzt und 1 der rechte y wert)
        if (directions[i]=='<'):
            Ort_jetzt.append((letzter_Wert[0]-1, letzter_Wert[1]))
        if (directions[i]=='^'):
            Ort_jetzt.append((letzter_Wert[0], letzter_Wert[1]+1))
        if (directions[i]=='v'):
            Ort_jetzt.append((letzter_Wert[0], letzter_Wert[1]-1))

    return len(set(Ort_jetzt))

einzigartige_Häuser=Ortsberechnung(einlesen())
print(f"Der Weihnachtsmann muss {einzigartige_Häuser} Häuser besuchen")