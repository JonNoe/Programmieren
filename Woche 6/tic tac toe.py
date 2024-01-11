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
            Zug_Spieler = int(Zug_Spieler)-1
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
    
def main():
    print('Um zu Spielen geben Sie eine Zahl zwischen 1 und 9 ein, um im jeweiligen Feld ein X zu setzen')
    print('Tipp: Sie können das Spiel jederzeit beeneden, indem Sie "Quit" eingeben')
    feld_erstellen()
    global spieler_aktuell
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
        Wechsel_Spieler()
        
            
        
    
    

if __name__ == '__main__':
    main()