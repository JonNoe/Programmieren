import re
import numpy as np

with open ('D:\DHBW\Programmieren\Repo\Programmieren\Woche 5\Input 6.txt') as file:
    Regelungen = file.read().split('\n')    
file.close()

Lichterquadrat = np.full((1000,1000),False)
