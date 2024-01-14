import random

# Problem war den Vektor zum simulieren mit dem feldvektor gleichzusetzen --> hatten die selbe adresse und so hat sich auch das gespielte feld verändert
# nicht nur das simulierte
# Lösung: eine neue Liste erstellen, der man die selbe bestandteile gibt

# Fehler mit schwachem bot:
# er hat das Falsche feld gelesen und dann auch mit falschem Index eingetragen

#Konstanten definiert
SPIELER_ZEICHEN = 'X'
COMPUTER_ZEICHEN = 'O'
#start mit es wird gespielt
spielen = True
#Feld zum verändern
feld = ['1','2','3',
        '4','5','6',
        '7','8','9']
ursprüngliches_feld = ['1','2','3',
                       '4','5','6',
                       '7','8','9']
aktuelles_Feld = []
#wer spielt
spieler_aktuell = 'Computer'

def feld_erstellen():
    
    print(ursprüngliches_feld[0] + '|' + ursprüngliches_feld[1] + '|' + ursprüngliches_feld[2])
    print(ursprüngliches_feld[3] + '|' + ursprüngliches_feld[4] + '|' + ursprüngliches_feld[5])
    print(ursprüngliches_feld[6] + '|' + ursprüngliches_feld[7] + '|' + ursprüngliches_feld[8])
    
def feld_ausgabe(Zug_s):
    global spieler_aktuell
    if spieler_aktuell == 'Mensch':
        zeichen = SPIELER_ZEICHEN
    else:
        zeichen = COMPUTER_ZEICHEN
        
    feld[Zug_s] = zeichen #hier geändert -1 weg
    print(feld[0] + '|' + feld[1] + '|' + feld[2])
    print(feld[3] + '|' + feld[4] + '|' + feld[5])
    print(feld[6] + '|' + feld[7] + '|' + feld[8])


def spieler_eingabe():
    global spielen
    while spielen == True:
        Zug_Spieler = input('In welchem Feld wollen Sie spielen: ').lower()
        if Zug_Spieler == 'quit':
            spielen = False
            return 
        try:
            Zug_Spieler = int(Zug_Spieler) -1
            if position_spielbar(Zug_Spieler):
                print('Das Feld ist bereits belegt, bitte wählen Sie ein anderes Feld')
                continue
        except ValueError:
            print('Zahl Auserhalb des zahlenbereichs 1-9')
        if Zug_Spieler >= 0 and Zug_Spieler < 9:
            return Zug_Spieler
        else: 
            print('Bitte geben Sie eine Zahl zwischen 1 und 9 ein')

def position_spielbar(position):
    if  not feld[position ] == ursprüngliches_feld[position]:
        return True
    return False
    
def Computer_Zug():
    global aktuelles_Feld
    bestScore = -800
    bestmove = 0

    while spieler_aktuell == 'Computer':
        for i in range(len(feld)):
            aktuelles_Feld.append(feld[i])
            #print(aktuelles_Feld)
        for key in range(len(feld)):
            print(key)
            if position_spielbar(key): #position_spielbar(key)
                continue
            else:
                aktuelles_Feld[key] = COMPUTER_ZEICHEN
                #print(aktuelles_Feld)
                score = minimax(aktuelles_Feld, False)
                aktuelles_Feld[key] = ursprüngliches_feld[key]
                if score > bestScore:
                    bestScore = score
                    bestmove = key
        Computer_Zug = bestmove
        aktuelles_Feld = []
        feld_ausgabe(bestmove)    
        return Computer_Zug



def minimax(feld_aktuell, isMaximizing):
    if check_wer_gewonnen(COMPUTER_ZEICHEN):
        return 1
    elif check_wer_gewonnen (SPIELER_ZEICHEN):
        return -1
    elif Kontrolle_Unentschieden():
        return 0
    
    if isMaximizing: #maximizing
        bestScore = -800
        for key in range(len(feld_aktuell)):
            if feld_aktuell[key] == ursprüngliches_feld[key]:
                feld_aktuell[key] = COMPUTER_ZEICHEN
                score = minimax(feld_aktuell, False)
                feld_aktuell[key] = ursprüngliches_feld[key]
                if score > bestScore:
                    bestScore = score
        return bestScore
    
    else: #minimizing
        bestScore = 800
        for key in range(len(feld_aktuell)):
            if feld_aktuell[key] == ursprüngliches_feld[key]:
                feld_aktuell[key] = SPIELER_ZEICHEN
                score = minimax(feld_aktuell,True)
                feld_aktuell[key] = ursprüngliches_feld[key]
                if score < bestScore:
                    bestScore = score
        return bestScore
                
        
                          
def Wechsel_Spieler():
    global spieler_aktuell
    if spieler_aktuell == 'Mensch':
        spieler_aktuell = 'Computer'        
    else:
        spieler_aktuell = 'Mensch'


def Kontrolle_Unentschieden():
    if ((feld[0] == 'X' or feld[0] == 'O')  \
        and (feld[1] == 'X' or feld[1] == 'O')  \
        and (feld[2] == 'X' or feld[2] == 'O')  \
        and (feld[3] == 'X' or feld[3] == 'O')  \
        and (feld[4] == 'X' or feld[4] == 'O')  \
        and (feld[5] == 'X' or feld[5] == 'O')  \
        and (feld[6] == 'X' or feld[6] == 'O')  \
        and (feld[7] == 'X' or feld[7] == 'O')  \
        and (feld[8] == 'X' or feld[8] == 'O')):
            return True
    else: return False

def check_wer_gewonnen(zeichen):
    #Kontrolle Zeilen
    if feld[0] == feld[1] == feld[2] == zeichen:
        return True
    if feld[3] == feld[4] == feld[5] == zeichen:
        return True
    if feld[6] == feld[7] == feld[8] == zeichen:
        return True
    #Kontrolle Spalten
    if feld[0] == feld[3] == feld[6] == zeichen:
        return True
    if feld[1] == feld[4] == feld[7] == zeichen:
        return True
    if feld[2] == feld[5] == feld[8] == zeichen:
        return True
    #Kontrolle Diagonale
    if feld[0] == feld[4] == feld[8] == zeichen:
        return True
    if feld[2] == feld[4] == feld[6] == zeichen:
        return True


def main():
    print('Um zu Spielen geben Sie eine Zahl zwischen 1 und 9 ein, um im jeweiligen Feld ein X zu setzen')
    print('Tipp: Sie können das Spiel jederzeit beeneden, indem Sie "Quit" eingeben')
    feld_erstellen()
    global spieler_aktuell
    global spielen
    while spielen == True:
        if spieler_aktuell == 'Mensch':
            zeichen = SPIELER_ZEICHEN
        else:
            zeichen = COMPUTER_ZEICHEN
        print(f'{spieler_aktuell} ist am Zug')
        if spieler_aktuell == 'Mensch':
            Zug_spieler = spieler_eingabe()             
            feld_ausgabe(Zug_spieler)
            print(f'\nIhr Spielzug: {Zug_spieler} \n') 
        else:
            Zug_Computer = Computer_Zug()
            #feld_ausgabe(Zug_Computer)
            print(f'\nDer Computer hat in Feld {Zug_Computer+1} gespielt \n')
        #print(feld)
        #hat jemand gewonnen?
        gewonnen = check_wer_gewonnen(zeichen)
        if gewonnen:
            print(f'{spieler_aktuell} hat gewonnen')
            spielen = False
        unentschieden = Kontrolle_Unentschieden()
        if unentschieden:
            print('Die Partie ist unentschieden ausgegangen')
            spielen = False
        #Am Ende des Zuges Spielerwechsel
        Wechsel_Spieler()
        
if __name__ == '__main__':
    main()