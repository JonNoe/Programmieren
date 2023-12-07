#kleines Programm, dass aus * einen Baum baut

#Funktion die die Anzahl der * und Leerzeichen bestimmt
def print_christmastree(height):
    for i in range(0,height,1):
        stars = "*" * (2*i+1)
        spaces = " " * (height - i - 1)
        print(spaces+stars)

#Angabe Höhe 
height = 3
#Funktionsaufruf
print_christmastree(height)