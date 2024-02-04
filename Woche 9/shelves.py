import shelve

d = shelve.open('Daten.txt')
d['Frucht'] = 'Apfel'
d.close()

d = shelve.open('Daten.txt')
Frucht = d['Frucht'] 
d.close()

print(f'Die in der Datei gespeicherte Frucht ist: \n{Frucht}')