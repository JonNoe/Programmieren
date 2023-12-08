#kleines Programm, dass aus * einen Baum baut

Sternenliste = []

#Funktion die die Anzahl der * und Leerzeichen bestimmt
def print_christmastree(height):
    for i in range(0,height,1):
        anzahl = 2*i+1
        stars = "*" * anzahl
        Sternenliste.append(anzahl)
        spaces = " " * (height - i - 1)
        print(spaces+stars)
    if (height < 4):
        for i in range (0,int(height/3),1):
            spaces = " " *(height-1)
            stamm = "|"
            print(spaces+stamm)
    if (height < 40 ):
        for i in range(0,int(height/3),1):
            spaces = " " * int(max(Sternenliste)/2-height/6)
            stamm = "|" * int(height/3)
            print(spaces+stamm)
    else :
        for i in range(0,int(height/3),1):
            spaces = " " * int(max(Sternenliste)/2-height/7)
            stamm = "|" * int(height/3)
            print(spaces+stamm)
    if (height > 60):
        print("Es kann vorkommen, dass der Stamm nicht mehr zentral ist")      
    
    
#Angabe Höhe 
print("Das ist ein Programm um einen Weihnachtsbaum zu erstellen")
height = abs(int(input("Wie hoch soll der Baum sein: ")))
#Funktionsaufruf
print_christmastree(height)