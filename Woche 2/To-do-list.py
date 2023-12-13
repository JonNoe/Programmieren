to_do = ['Monster Hunter spielen']

def Liste_hinzufügen(was_hinzufuegen):
    to_do.append(was_hinzufuegen)

def Liste_loeschen(loeschen):
    to_do.remove(loeschen.lower())


weiter = 1
if(input("Soll die aktuelle Liste wiedergegeben werden? ").lower()=='ja'):
    print(to_do)
hinzufuegen = input("Möchtest du etwas zu deiner to do list hinzufügen? ")
if (hinzufuegen.lower() == "ja"):
    while(weiter==1):
        was_hinzufuegen=input("Was möchtest du hinzufügen? ")
        Liste_hinzufügen(was_hinzufuegen)
        noch_etwas_hinzufuegen=input("Möchtest du noch etwas hinzufügen?").lower()
        if (noch_etwas_hinzufuegen!='ja'):
            weiter=0

    
    
weiter=1
loeschen=input("Hast du etwas erledigt oder möchtest etwas streichen? ")
if(loeschen.lower() == "ja"):
    while(weiter==1):
        was_loeschen=input("Was möchtest du streichen? ").lower()
        if was_loeschen in to_do:
            Liste_loeschen(was_loeschen)
        else:
            print("Objekt nicht gefunden")
        noch_etwas_streichen=input("Möchtest du noch etwas streichen? ").lower()
        if (noch_etwas_streichen!='ja'):
            weiter=0


if(input("Soll die aktuelle Liste wiedergegeben werden? ").lower()=='ja'):
    print(to_do)



