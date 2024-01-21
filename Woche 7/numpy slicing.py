import numpy as np
#2 dimensionaler array
arr = np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(arr)

#ausgabe an bestimmter stelle
print(arr[0,0])
#gibt lände des arrays aus
print(np.size(arr))
länge = int(np.size(arr)/2)

#Ausgabe der Werte einzeln
for i in range(2): #Angabe der Zeilen
    for j in range(länge): #Spalten
        print(arr[i,j])
        
print() #Leerzeile
        
print(arr[1,1:4]) #gibt aus Zeile 2 spalten mit index 1-3 aus
print(arr[:,:]) #ganzer array
print(arr[0:2,0:3]) #2. Zahl - 1. Zahl = Ausgegebene Elemente ab der Index der 1. Zahl
#typenausgabe
print(f'Der array ist von Typ {arr.dtype}')

#Arraytypes
#Array in boolische Werte 
newarray = arr.astype(bool)
print(newarray)
print(f'Der array ist von Typ {newarray.dtype}')
