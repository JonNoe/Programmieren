
def name():
    name=[]
    Leerzeichen=[]
    voller_name= input("Bitte geben Sie ihren vollen Namen ein: ")
    Zahl_Leer=voller_name.count(" ")
    
    for i in range(0,Zahl_Leer):
        Leerzeichen.append(voller_name.find(" ",i))
        
        
    #vorname=voller_name[:Leerzeichen].capitalize()
    for x in Leerzeichen:
        namen=[voller_name[:x]]
        #name.append(voller_name[Leerzeichen[0]+1:Leerzeichen[j+1]+2].capitalize())
    #print(vorname)
    print(Zahl_Leer)
    print(Leerzeichen)
    print(namen)


def website(websites):
    gekürzt = slice(12,-5)
    for seite in websites:
        print(seite[gekürzt])
    
name()


websites=['https://www.google.com/']
weiter=True
while (weiter):
    webseiten=input("Geben Sie eine Webseite ein: ")
    websites.append(webseiten)
    mehr_websites=input("Wollen Sie noch mehr webseiten hinzufügen? ").lower()
    if (mehr_websites != 'ja'):
        weiter=False
    
website(websites)