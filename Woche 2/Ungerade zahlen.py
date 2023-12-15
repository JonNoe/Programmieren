#Bereich auskommentieren: strg + K, danach C
#Rückgängig: strg + K, danach U

#Hilfe für Listen
# print(dir(zahlen))
# print(help(zahlen))

def ungerade_zahlen(von,bis):
    zahlen = list(range(von,bis))
    ung_zahlen=zahlen[0:len(zahlen):2]
    return ung_zahlen


print("In Welchem Bereich möchten Sie die ungeraden zahlen ausgegeben haben? ")
von=int(input("Von: "))
bis=int(input("Bis: "))
print(ungerade_zahlen(von,bis))

print(ungerade_zahlen(von,bis)[::-1]) # reverse manuell

# reverse mit befehl aber befehl geht net :(
# rückwärts=(ungerade_zahlen(von,bis).reverse)
# print(rückwärts)
