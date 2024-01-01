import re
import numpy as np

with open ('C:\\Users\jonin\Documents\Programmieren\Programmieren Repo\Weekly\Programmieren\Woche 5\input 6.txt') as file:
    Regelungen = file.read().split('\n')  
    Zeilenzahl = len(Regelungen)  
file.close()

Lichterquadrat = np.full((1000,1000),False)
for Anweisungen in Regelungen:
    wörter = Anweisungen.split()
    
    x1, y1 =  map(int, wörter[-3].split(','))
    x2, y2 = map(int, wörter[-1].split(','))
    
    if Anweisungen.startswith('turn on'):
        Lichterquadrat[x1:x2+1,y1:y2+1] = 1
    
    if Anweisungen.startswith('turn off'):
        Lichterquadrat[x1:x2+1, y1:y2+1] = 0
        
    if Anweisungen.startswith('toggle'):
        Lichterquadrat[x1:x2+1, y1:y2+1] = 1- Lichterquadrat[x1:x2+1, y1:y2+1]  #dreht 1 zu 0 und  zu 1
    
print(f'Es sind {Lichterquadrat.sum()} Lichter an')  
        
    
    
