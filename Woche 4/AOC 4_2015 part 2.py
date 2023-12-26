from hashlib import md5
from itertools import count
code = 'ckczppom' #mein eigener code
for i in count(1): #count(1) = alle verschiedenen möglichkeiten ausprobieren
    testen = code + str(i) #beide zusammenhängen
    if md5(testen.encode('utf-8')).hexdigest()[:6]=='000000': #encoden von jeder kombination in hexadezimalzahl, bis die ersten 6 Stellen alle 0 sind
        print(i)
        break