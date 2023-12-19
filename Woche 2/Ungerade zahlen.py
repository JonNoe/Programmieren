import math
#Bereich auskommentieren: strg + K, danach C
#Rückgängig: strg + K, danach U

#Hilfe für Listen
# print(dir(zahlen))
# print(help(zahlen))
ung_zahlen=[]
def ungerade_zahlen(von,bis):
    zahlen = list(range(von,bis))
    #ung_zahlen=zahlen[0:len(zahlen):2]
    for i in range (0,bis-von):
        if (zahlen[i] % 2!=0):
            ung_zahlen.append(zahlen[i]) 
    
    return ung_zahlen


print("In Welchem Bereich möchten Sie die ungeraden zahlen ausgegeben haben? ")
von=int(input("Von: "))
bis=int(input("Bis: "))
print(ungerade_zahlen(von,bis))


#print(ungerade_zahlen(von,bis)[::-1]) # reverse manuell

# reverse mit befehl aber befehl geht net :(
# rückwärts=(ungerade_zahlen(von,bis).reverse)
# print(rückwärts)
