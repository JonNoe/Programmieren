import random
MÜNZE = ['kopf','zahl']
Spiel_aktiv = True

def Coinflip():
    print('\nDie Münze wird geworfen')
    print('...')
    Wahl_Spieler = input('Wie wird die Münze landen? ').lower()
    if Wahl_Spieler not in MÜNZE:
        print('Bitte geben Sie entweder Kopf oder Zahl ein und versuchen Sie es erneut')
        return
    Ergebnis = random.choice(MÜNZE)
    print(f'Die münze ist auf {Ergebnis} gelandet')
    if Wahl_Spieler == Ergebnis:
        print('Du hast gewonnen')
    else:
        print('Du hast leider verloren')
    
        
    

def main():
    global Spiel_aktiv
    while Spiel_aktiv == True:
        Coinflip()
        neues_Spiel = input('\nMöchtest du erneut spielen? ').lower()
        if neues_Spiel != 'ja':
            Spiel_aktiv = False
    
    
if __name__ == '__main__':
    main()