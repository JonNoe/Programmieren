from PyDictionary import PyDictionary

dictionary = PyDictionary() #Die englische Bibliothek wird benutzt

wort = input('englisches Wort, für das die Wortart und Definition gesucht werden soll: ')

definition = dictionary.meaning(wort)
if definition:
    print(f'Die Definition von {wort} ist:')
    for wortart, bedeutung in definition.items():
        print(f'{wortart}: {" ".join(bedeutung)}')
else: print(f'Es wurde leider keine Definition für {wort} gefunden')