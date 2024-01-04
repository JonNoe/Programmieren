import re 
datei = 'D:\DHBW\Programmieren\Repo\Programmieren\Woche 5\\regex werte.txt'
with open (datei) as file:
    werte = file.read().split('\n')
file.close()

def Lösung_ohne():
    Volumen = 0    
    for zeile in werte:    
        laenge, breite, hoehe = zeile.split('x')
        print(laenge)
        laenge = int (laenge)
        breite = int(breite)
        hoehe = int(hoehe)
        #print (laenge, breite, hoehe)
        Volumen += laenge * breite* hoehe

    print(Volumen)

#oder
def Lösung_regex():
    Volumen_re = 0
    for zeile in werte:
        zahlen = re.split('x',zeile)
        laenge = int(zahlen[0])
        breite = int(zahlen[1])
        hoehe = int(zahlen[2])
        Volumen_re += laenge * breite* hoehe
    print(Volumen_re)

Lösung_regex()

def Vokale_raussuchen():
    Input = 'Hallo das ist der Input'
    Vokale = re.sub(r'[^aeiou]','',Input.lower()) # ^ ist ausser die Buchstaben
    #tauscht alle buchtaben mit nichts aus ausser die Vokale
    print(Vokale)

Vokale_raussuchen()