import string, secrets

def generate_Passwort(laenge):
    zeichen = string.ascii_letters +string.digits + string.punctuation
    sicheres_passwort = ''.join(secrets.choice(zeichen) for i in range(laenge))
    return sicheres_passwort

def main():
    laenge = int(input('Bitte geben Sie die Länge des Passworts ein:'))
    generiertes_passwort =generate_Passwort(laenge)
    print(generiertes_passwort)

if __name__ == '__main__':
    main()
