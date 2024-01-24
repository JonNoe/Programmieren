import pygame, sys, random
from pygame.math import Vector2

class Schlange:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)] #Kreiert Schlangenkörper
        self.Richtung = Vector2(1,0)
        self.Verlängerung = False
    
    def Schlange_bewegen(self):
        if self.Verlängerung == True:
            Körper_copy = self.body[:] #Kopiert alle
            Körper_copy.insert(0,Körper_copy[0] + self.Richtung) #Fügt am Kopf den Kopf der Schlange hinzu in Richtung von self.Richtung
            self.body = Körper_copy
            self.Verlängerung = False
            
        else:
            Körper_copy = self.body[:-1] #Kopiert alle außer den letzten Wert
            Körper_copy.insert(0,Körper_copy[0] + self.Richtung) #Fügt am Kopf den Kopf der Schlange hinzu in Richtung von self.Richtung
            self.body = Körper_copy
            

    def Schlange_malen(self):
        for Körperteil in self.body:
            x_pos = int(Körperteil.x) * Zellengroesse #Positionierung x-Achse Schlange
            y_pos = int(Körperteil.y) * Zellengroesse #Positionierung y-Achse Schlange
            Körperteil_rect = pygame.Rect(x_pos, y_pos, Zellengroesse, Zellengroesse)
            pygame.draw.rect(screen,pygame.Color('purple'),Körperteil_rect)

    def Schlange_verlängern(self):
        self.Verlängerung = True

            
class Frucht: 
    def __init__(self):
        self.random_fruit()
    
    def Frucht_malen(self):
        frucht_rect = pygame.Rect(int(self.pos.x * Zellengroesse), int(self.pos.y * Zellengroesse), Zellengroesse, Zellengroesse) #!!! Rect wird großgeschrieben
        pygame.draw.rect(screen,pygame.Color('red'),frucht_rect)

    def random_fruit(self):
        self.x = random.randint(0, Anzahl_Zellen - 1)
        self.y = random.randint(0, Anzahl_Zellen - 1)
        self.pos = Vector2(self.x,self.y)

class MAIN:
    def __init__(self):
        self.schlange = Schlange()
        self.frucht = Frucht ()


    def Update(self):
        self.schlange.Schlange_bewegen()
        self.Kollisionen()
    
    def Malen(self):
        main_game.frucht.Frucht_malen()
        main_game.schlange.Schlange_malen()
    
    def Kollisionen(self):
        if self.frucht.pos == self.schlange.body[0]:
            self.frucht.random_fruit()
            self.schlange.Schlange_verlängern()


pygame.init()
Zellengroesse = 40   
Anzahl_Zellen = 20

screen = pygame.display.set_mode((Zellengroesse*Anzahl_Zellen,Zellengroesse*Anzahl_Zellen)) #Legt fenstergröße fest Breite*Höhe
clock = pygame.time.Clock()
FPS = 60


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()
global schlange
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Kontrolliert ob auf das x gedrückt wurde
            pygame.quit() #Fenster schließen
            sys.exit() #beendet allen Code
        if event.type == SCREEN_UPDATE:
            main_game.Update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.schlange.Richtung = Vector2(0, -1)

            if event.key == pygame.K_DOWN:
                main_game.schlange.Richtung = Vector2(0, 1)

            if event.key == pygame.K_LEFT:
                main_game.schlange.Richtung = Vector2(-1, 0)
                
            if event.key == pygame.K_RIGHT:
                main_game.schlange.Richtung = Vector2(1, 0)

                
    screen.fill(pygame.Color((178,255,102)))
    main_game.Malen()
    pygame.display.update() #Updatet nach jedem while loop
    clock.tick(FPS) #updatet 30x pro sekunde
