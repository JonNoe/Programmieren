import re
import sys

Anzahl_richtiger_Strings = 0
Anzahl_richtiger_Strings_2 = 0
verbotene_Liste = ['ab','cd', 'pq','xy']
def nice_String(strings):
    
    #Vokale
    if len(re.sub(r'[^aeiou]','',strings)) <3:
        return False

    #Kommt zweimal vor
    if not re.search(r'(.)\1',strings):
        return False
    #In verbotener Liste
    for nw in verbotene_Liste:
        if nw in strings:
            return False
    return True

def part2(strings):
    #2 mal das selbe
    if not re.search(r'(.)(.).*\1\2',strings):
        return False
    #selber Buchstabe hintereinander
    if not re.search(r'(.).\1',strings):
        return False
    
    return True

def main ():   
    path = 'D:\DHBW\Programmieren\Repo\Programmieren\Woche 4\Input 5.txt'
    with open(path,'r') as file:
        for line in file:      
            if nice_String(line) == True:
                global Anzahl_richtiger_Strings
                Anzahl_richtiger_Strings += 1
            
            if part2(line):
                global Anzahl_richtiger_Strings_2
                Anzahl_richtiger_Strings_2 += 1
                
    
main()
print(f'Es sind {Anzahl_richtiger_Strings} der nicen Strings vorhanden')
print(f'Es sind {Anzahl_richtiger_Strings_2} der nicen Strings 2 vorhanden')

            
