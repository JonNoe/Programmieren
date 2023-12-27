import re

Anzahl_richtiger_Strings = 0
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


def main ():   
    path = 'D:\DHBW\Programmieren\Repo\Programmieren\Woche 4\Input 5.txt'
    with open(path,'r') as file:
        for line in file:      
            if nice_String(line) == True:
                global Anzahl_richtiger_Strings
                Anzahl_richtiger_Strings += 1
        

main()
print(f'Es sind {Anzahl_richtiger_Strings} der nicen Strings vorhanden')
            

    



        
        
    
