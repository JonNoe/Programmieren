# breite=int(input("Welche Breite sollen die Dreiecke haben? "))

# anzahl=[]
# for i in range (breite):
#     anzahl.append(i)
#     spaces = ' ' * (breite-i+3)
#     print("x"*anzahl[i]+2*spaces+"o"*anzahl[i])
# for i in range(breite,-1,-1):
#     anzahl.append(i)
#     spaces = ' ' * (breite-i+3)
#     print("x"*anzahl[i]+2*spaces+"o"*anzahl[i])
    

backslash =[]    
hoehe= int(input("Welche Höhe sollen die Triforce haben? "))
for i in range (0,hoehe):
    zahl=2*i
    backslash.append(i)
    spaces = " " * (hoehe - i - 1)
    print(spaces+'/'+' '*2*i+'\\')

