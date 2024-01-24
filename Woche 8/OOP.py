class Personendaten:
    def __init__(self,geschlecht,alter,größe):
        self.geschlecht = geschlecht
        self.alter = alter
        self.größe = größe
        
 
 
def main():
    geschlecht = input('Geben Sie ihr Geschlecht an: ').lower()
    alter = input('Geben Sie ihr Alter an: ')
    größe = input('Geben Sie ihre Größe in m an: ')
    
    Person_1 = Personendaten(geschlecht,alter,größe)
    print('Sie sind '+ Person_1.geschlecht+', ' + Person_1.alter + ' Jahre alt und ' + Person_1.größe + ' m groß')
    
if __name__ == '__main__':
    main()   