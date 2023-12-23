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

def Santa(directions):
    Ort_jetzt_Santa=[(0,0)] #Liste in Liste , da man beide variablen überschreiben will hier: links x rechts y
    richtungswechsel = len(directions)

    for i in range(0,richtungswechsel,2):
        letzter_Wert = Ort_jetzt_Santa[-1] #Kopiert den Endwert des letzten Durchgangs wie ein Speicher
        if (directions[i]=='>'):
            Ort_jetzt_Santa.append((letzter_Wert[0]+1, letzter_Wert[1])) #hier x wert des letzten durchgangs +1 (letzter_Wert[0] ist der linke Wert von ort_jetzt und 1 der rechte y wert)
        if (directions[i]=='<'):
            Ort_jetzt_Santa.append((letzter_Wert[0]-1, letzter_Wert[1]))
        if (directions[i]=='^'):
            Ort_jetzt_Santa.append((letzter_Wert[0], letzter_Wert[1]+1))
        if (directions[i]=='v'):
            Ort_jetzt_Santa.append((letzter_Wert[0], letzter_Wert[1]-1))
    return Ort_jetzt_Santa

def Robo(directions):
    Ort_jetzt_Robo=[(0,0)] #Liste in Liste , da man beide variablen überschreiben will hier: links x rechts y
    richtungswechsel = len(directions)

    for i in range(1,richtungswechsel,2):
        letzter_Wert = Ort_jetzt_Robo[-1] #Kopiert den Endwert des letzten Durchgangs wie ein Speicher
        if (directions[i]=='>'):
            Ort_jetzt_Robo.append((letzter_Wert[0]+1, letzter_Wert[1])) #hier x wert des letzten durchgangs +1 (letzter_Wert[0] ist der linke Wert von ort_jetzt und 1 der rechte y wert)
        if (directions[i]=='<'):
            Ort_jetzt_Robo.append((letzter_Wert[0]-1, letzter_Wert[1]))
        if (directions[i]=='^'):
            Ort_jetzt_Robo.append((letzter_Wert[0], letzter_Wert[1]+1))
        if (directions[i]=='v'):
            Ort_jetzt_Robo.append((letzter_Wert[0], letzter_Wert[1]-1))

    return Ort_jetzt_Robo

einzigartige_Orte_Santa = Santa(einlesen())
einzigartige_Orte_Robo = Robo(einlesen())
einzigeartige_Orte=set(einzigartige_Orte_Santa+einzigartige_Orte_Robo)
print(len(einzigeartige_Orte))