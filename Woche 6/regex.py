import re

def inport_file():
    Datei = 'C:\\Users\jonin\Documents\Programmieren\Programmieren Repo\Weekly\Programmieren\Woche 6\Beispieltext.txt'
    with open (Datei) as file:
        text = file.read().split('\n')
    file.close
    return text

def main ():
    text = inport_file()
    Vokale = r'[^aeiou]' #startet nicht mit einem Vokal
    for i in text:
        
        #print(i)
        Vokalstart=re.sub(Vokale,' ',str(i))
        print(Vokalstart)

if __name__ == '__main__':
    main()