import random

def random_name():
    vornamen = ["Ichigo","Naruto","Goku","Sakura","Luffy","Hinata","Sasuke","Eren","Mikasa","Asuna","Kirito","Nami","Vegeta","Rukia","Kakashi"]
    nachnamen = [    "Uzumaki","Kurosaki","Son","Haruno","Monkey D.","Hyuga","Uchiha","Yeager","Ackerman","Yuuki","Kirigaya","Nami","Brief","Kuchiki","Hatake"]
    return random.choice(nachnamen) + ' '  + random.choice(vornamen)

Anzahl = int(input('Anzahl der zu generierenden Namen eingeben: '))
for i in range(Anzahl):
    print(random_name())
print('\nDie Reihenfolge der Namen im Japanischen ist vertauscht, daher steht der Nachname vor dem Vornamen\n')
