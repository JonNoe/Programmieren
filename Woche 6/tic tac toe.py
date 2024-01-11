import random
#Konstanten definiert
SPIELER_ZEICHEN = 'X'
COMPUTER_ZEICHEN = 'O'
#start mit es wird gespielt
spielen = True
#Feld zum verändern
feld = ['1','2','3',
        '4','5','6',
        '7','8','9']
#wer spielt
spieler_aktuell = 'Mensch'

def feld_erstellen():
    
    print(feld[0] + '|' + feld[1] + '|' + feld[2])
    print(feld[3] + '|' + feld[4] + '|' + feld[5])
    print(feld[6] + '|' + feld[7] + '|' + feld[8])
    
def feld_ausgabe(Zug_s):
    global spieler_aktuell
    if spieler_aktuell == 'Mensch':
        zeichen = SPIELER_ZEICHEN
    else:
        zeichen = COMPUTER_ZEICHEN
        
    feld[Zug_s-1] = zeichen
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
            Zug_Spieler = int(Zug_Spieler)
            if feld[Zug_Spieler-1] == 'X' or feld[Zug_Spieler-1] == 'O':
                print('Das Feld ist bereits belegt, bitte wählen Sie ein anderes Feld')
                continue
        except ValueError:
            print('Zahl Auserhalb des zahlenbereichs 1-9')
        if Zug_Spieler > 0 and Zug_Spieler < 10:
            return Zug_Spieler
        else: 
            print('Bitte geben Sie eine Zahl zwischen 1 und 9 ein')

def Computer_Zug():
    while spieler_aktuell == 'Computer':
        Zug_Computer = random.randint(1,9)
        if feld[Zug_Computer-1] == 'X' or feld[Zug_Computer-1] == 'O':
            continue
        else:
            return Zug_Computer
        
                          
def Wechsel_Spieler():
    global spieler_aktuell
    if spieler_aktuell == 'Mensch':
        spieler_aktuell = 'Computer'        
    else:
        spieler_aktuell = 'Mensch'

def Kontrolle_Gewonnen():
    #Kontrolle Zeilen
    if feld[0] == feld[1] == feld[2]:
        return feld [0]
    if feld[3] == feld[4] == feld[5]:
        return feld [3]
    if feld[6] == feld[7] == feld[8]:
        return feld [6]
    #Kontrolle Spalten
    if feld[0] == feld[3] == feld[6]:
        return feld [0]
    if feld[1] == feld[4] == feld[7]:
        return feld [1]
    if feld[2] == feld[5] == feld[8]:
        return feld [2]
    #Kontrolle Diagonale
    if feld[0] == feld[4] == feld[8]:
        return feld [0]
    if feld[2] == feld[4] == feld[6]:
        return feld [2]

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


def main():
    print('Um zu Spielen geben Sie eine Zahl zwischen 1 und 9 ein, um im jeweiligen Feld ein X zu setzen')
    print('Tipp: Sie können das Spiel jederzeit beeneden, indem Sie "Quit" eingeben')
    feld_erstellen()
    global spieler_aktuell
    global spielen
    while spielen == True:
        print(f'{spieler_aktuell} ist am Zug')
        if spieler_aktuell == 'Mensch':
            Zug_spieler = spieler_eingabe()             
            feld_ausgabe(Zug_spieler)
            print(f'Ihr Spielzug: {Zug_spieler} \n') 
        else:
            Zug_Computer = Computer_Zug()
            feld_ausgabe(Zug_Computer)
            print(f'Der Computer hat in Feld {Zug_Computer} gespielt \n')
        #hat jemand gewonnen?
        gewonnen = Kontrolle_Gewonnen()
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