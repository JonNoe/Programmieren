import pygame, sys, random
from pygame.math import Vector2
from button import Button
pygame.init()

programIcon = pygame.image.load("Körper_Schlange\Snake_Symbol.PNG")
pygame.display.set_icon(programIcon)

Fenster = pygame.display.set_mode((800,600) ,0,24)
pygame.display.set_caption("Projekt: Snake")


class Schlange:
    def __init__(self):
        self.body = [Vector2(5,7),Vector2(4,7),Vector2(3,7)] #Kreiert Schlangenkörper
        self.Richtung = Vector2(0,0)
        self.Verlängerung = False
        
        self.Kopf_links = pygame.image.load('Körper_Schlange\Kopf_links.png').convert_alpha()        #kreiert die Kopfanimation
        self.Kopf_rechts = pygame.image.load('Körper_Schlange\Kopf_rechts.png').convert_alpha()
        self.Kopf_oben = pygame.image.load('Körper_Schlange\Kopf_unten.png').convert_alpha()
        self.Kopf_unten = pygame.image.load('Körper_Schlange\Kopf_oben.png').convert_alpha()

        self.Körper_LO = pygame.image.load('Körper_Schlange\LO.png').convert_alpha()                 # kreiert die Körperanimation
        self.Körper_RO = pygame.image.load('Körper_Schlange\RO.png').convert_alpha()
        self.Körper_LU = pygame.image.load('Körper_Schlange\LU.png').convert_alpha()
        self.Körper_RU = pygame.image.load('Körper_Schlange\RU.png').convert_alpha()

        self.Schwanz_rechts = pygame.image.load('Körper_Schlange\Schwanz_links.png').convert_alpha()  # kreiert die Schwanzanimation
        self.Schwanz_links = pygame.image.load('Körper_Schlange\Schwanz_rechts.png').convert_alpha()
        self.Schwanz_unten = pygame.image.load('Körper_Schlange\Schwanz_unten.png').convert_alpha()
        self.Schwanz_oben = pygame.image.load('Körper_Schlange\Schwanz_oben.png').convert_alpha()

        self.Körper_links = pygame.image.load('Körper_Schlange\Korper_links.png').convert_alpha()    # kreiert die Körperanimation
        self.Körper_rechts = pygame.image.load('Körper_Schlange\\Korper_rechts.png').convert_alpha()
        self.Körper_unten = pygame.image.load('Körper_Schlange\Korper_unten.png').convert_alpha()
        self.Körper_oben = pygame.image.load('Körper_Schlange\Korper_oben.png').convert_alpha()

        self.oneup = pygame.mixer.Sound('Sounds\One_UP.mp3')
        self.oneup.set_volume(0.3)

 
    def Schlange_bewegen(self):
        if self.Verlängerung == True:
            Körper_copy = self.body[:] #Kopiert alle Körperteile
            Körper_copy.insert(0, Körper_copy[0] + self.Richtung) #Fügt am Kopf den Kopf der Schlange hinzu in Richtung von self.Richtung
            self.body = Körper_copy
            self.Verlängerung = False
            
        else:
            Körper_copy = self.body[:-1] #Kopiert alle außer den letzten Wert
            Körper_copy.insert(0, Körper_copy[0] + self.Richtung) #Fügt am Kopf den Kopf der Schlange hinzu in Richtung von self.Richtung
            self.body = Körper_copy
            

    def Schlange_malen(self):
        self.update_Kopf_Grafiken()
        self.update_Schwanz_Grafiken()

        for index, Körperteil in enumerate(self.body):
            x_pos = int(Körperteil.x) * Zellengroesse #Positionierung x-Achse Schlange
            y_pos = int(Körperteil.y) * Zellengroesse #Positionierung y-Achse Schlange
            Körperteil_rect = pygame.Rect(x_pos, y_pos, Zellengroesse, Zellengroesse)

            if index == 0:
                screen.blit(self.Kopf,Körperteil_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.Schwanz,Körperteil_rect)
            else:
                vorgänger = self.body[index + 1] - Körperteil
                folgender = self.body[index - 1] - Körperteil
                if vorgänger.x == folgender.x:
                    screen.blit(self.Körper_oben,Körperteil_rect) #macht bei hortizontal nur Körper unten
                elif vorgänger.y == folgender.y:
                    screen.blit(self.Körper_rechts,Körperteil_rect) #macht bei vertikal nur Körper unten
                else: #Ecken, wie hängen benachbarte Körperteile von dem Aktuellen ab
                    if vorgänger.x == -1 and folgender.y == -1 or vorgänger.y == -1 and folgender.x == -1:
                        screen.blit(self.Körper_RU, Körperteil_rect)
                    elif vorgänger.x == -1 and folgender.y == 1 or vorgänger.y == 1 and folgender.x == -1:
                        screen.blit(self.Körper_RO, Körperteil_rect)
                    elif vorgänger.x == 1 and folgender.y == 1 or vorgänger.y == 1 and folgender.x == 1:
                        screen.blit(self.Körper_LO, Körperteil_rect)
                    elif vorgänger.x == 1 and folgender.y == -1 or vorgänger.y == -1 and folgender.x == 1:
                        screen.blit(self.Körper_LU, Körperteil_rect)

        
    def update_Kopf_Grafiken(self):
        Kopf_abhängigkeiten = self.body[1] -self.body[0] #Findet heraus, wie sich der Kopf zum letzten Körperteil bewegt
        if Kopf_abhängigkeiten == Vector2(1,0):
            self.Kopf = self.Kopf_links
        elif Kopf_abhängigkeiten == Vector2(-1,0):
            self.Kopf = self.Kopf_rechts
        elif Kopf_abhängigkeiten == Vector2(0,-1):
            self.Kopf = self.Kopf_oben
        elif Kopf_abhängigkeiten == Vector2(0,1):
            self.Kopf = self.Kopf_unten
    
    def update_Schwanz_Grafiken(self):
        Schwanz_abhängigkeiten = self.body[-2] -self.body[-1] #Findet heraus, wie sich der Kopf zum letzten Körperteil bewegt
        if Schwanz_abhängigkeiten == Vector2(1,0):
            self.Schwanz = self.Schwanz_links
        elif Schwanz_abhängigkeiten == Vector2(-1,0):
            self.Schwanz = self.Schwanz_rechts
        elif Schwanz_abhängigkeiten == Vector2(0,-1):
            self.Schwanz = self.Schwanz_oben
        elif Schwanz_abhängigkeiten == Vector2(0,1):
            self.Schwanz = self.Schwanz_unten

    def Schlange_verlängern(self):
        self.Verlängerung = True
    
    def play(self):
        self.oneup.play()

    def reset(self):
        self.body = [Vector2(5,7),Vector2(4,7),Vector2(3,7)] 
        self.Richtung = Vector2(0,0)

            
class Frucht: 
    def __init__(self):
        self.random_fruit()
    
    def Frucht_malen(self):
        frucht_rect = pygame.Rect(int(self.pos.x * Zellengroesse), int(self.pos.y * Zellengroesse), Zellengroesse, Zellengroesse) #!!! Rect wird großgeschrieben
        screen.blit(komische_frucht,frucht_rect)

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
        self.Tod()
        self.check_fail()
  
        
    def Malen(self):
        self.Gras_Feld()
        self.Score()
        main_game.frucht.Frucht_malen()
        main_game.schlange.Schlange_malen()
        
    
    def Kollisionen(self):
        if self.frucht.pos == self.schlange.body[0]:
            self.frucht.random_fruit()
            self.schlange.Schlange_verlängern()
            self.schlange.play()
        
        for Körperteil in self.schlange.body[1:]: #Wenn Frucht Position in Körper der Schlange, dann erneut random
            if Körperteil == self.frucht.pos:
                self.frucht.random_fruit()


    def check_fail(self):   # Schlange trifft sich selbst oder rand, Spiel wird beendet
        if not 0 <= self.schlange.body[0].x < Anzahl_Zellen or not 0 <= self.schlange.body[0].y < Anzahl_Zellen:
            self.game_over()

        for Körperteil in self.schlange.body[1:]:
            if Körperteil == self.schlange.body[0]:
                 self.game_over()
                 

    def Tod(self): # Schlange trifft sich selbst oder rand, Spiel wird beendet
        global Todesart   
        if not 0 <= self.schlange.body[0].x < Anzahl_Zellen or not 0 <= self.schlange.body[0].y < Anzahl_Zellen: #Wenn nicht im feld
            Todesart = 1
            #print(Todesart)

        for Körperteil in self.schlange.body[1:]:
            if Körperteil == self.schlange.body[0] and not self.schlange.body[0] == Vector2(5, 7) and not self.schlange.body[1] == Vector2(4, 7) and not self.schlange.body[2] == Vector2(3,7):
                Todesart = 2
                #print(Todesart)

    def game_over(self):
        self.schlange.reset()

    def Gras_Feld(self):
    
        GRAS_FARBE = (167,255,61)
        for Zeile in range(Anzahl_Zellen):
            if Zeile % 2 == 0:
                for Zelle in range(Anzahl_Zellen):
                    if Zelle % 2 == 0:
                        grass_rect = pygame.Rect(Zelle * Zellengroesse, Zeile * Zellengroesse, Zellengroesse, Zellengroesse)
                        pygame.draw.rect(screen,GRAS_FARBE,grass_rect)
            else:
                for Zelle in range(Anzahl_Zellen):
                    if Zelle % 2 != 0:
                        grass_rect = pygame.Rect(Zelle * Zellengroesse, Zeile * Zellengroesse, Zellengroesse, Zellengroesse)
                        pygame.draw.rect(screen,GRAS_FARBE,grass_rect)

    def Score(self):
        current_score = str(len(self.schlange.body) - 3) #score startet nicht bei 3
        score_surface = SCHRIFTART.render(current_score, True, (56,74,12))
        score_x = int(Zellengroesse * Anzahl_Zellen - 60) #Wo Score Anzeige
        score_y = int(Zellengroesse * Anzahl_Zellen - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y)) #Macht ein rectangle um den Score, und platziert mittif davon
        frucht_rect = komische_frucht.get_rect(midright = (score_rect.left, score_rect.centery))
        hintergrund_rect = pygame.Rect(frucht_rect.left, frucht_rect.top, frucht_rect.width + score_rect.width, frucht_rect.height )

        pygame.draw.rect(screen, (0, 255, 0), hintergrund_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(komische_frucht, frucht_rect)

        
        
BG = pygame.image.load("Hintergrund/Background.png")
#SCREEN = pygame.display.set_mode((1280, 720))

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Fonts/font.ttf", size)

def play():
    pygame.display.set_caption("Paly")
    global Todesart
    Todesart = 0
    spielen = True
    while spielen: #Game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Kontrolliert ob auf das x gedrückt wurde
                pygame.quit() #Fenster schließen
                sys.exit() #beendet allen Code
            if event.type == SCREEN_UPDATE:
                main_game.Update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: #Steuerung
                    if main_game.schlange.Richtung.y != 1: #Man kann nur nach oben gehen, wenn man nicht nach unten geht
                        main_game.schlange.Richtung = Vector2(0, -1)

                if event.key == pygame.K_DOWN:
                    if main_game.schlange.Richtung.y != -1:
                        main_game.schlange.Richtung = Vector2(0, 1)

                if event.key == pygame.K_LEFT:
                    if main_game.schlange.Richtung.x != 1:
                        main_game.schlange.Richtung = Vector2(-1, 0)
                    
                if event.key == pygame.K_RIGHT:
                    if main_game.schlange.Richtung.x != -1:
                        main_game.schlange.Richtung = Vector2(1, 0)
        
        screen.fill(pygame.Color((178,255,102)))
        main_game.Malen()
        pygame.display.update() #Updatet nach jedem while loop
        clock.tick(FPS) #updatet 30x pro sekunde
        if Todesart != 0:
            spielen = False
            restart()   


def main_menu():
    pygame.display.set_caption("Main Menu")
    global Todesart
    while True:
        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(50).render("SNAKE GAME", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center = (300, 100))

        PLAY_BUTTON = Button(image = pygame.image.load("Hintergrund/Play Rect.png"), pos = (300, 250), 
                            text_input = "PLAY", font = get_font(50), base_color="#d7fcd4", hovering_color = "White")
        #OPTIONS_BUTTON = Button(image=pygame.image.load("Hintergrund/Options Rect.png"), pos=(300, 250), 
                            #text_input="OPTIONS", font = get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image = pygame.image.load("Hintergrund/Quit Rect.png"), pos = (300, 450), 
                            text_input = "SCHLIEßEN", font = get_font(50), base_color="#d7fcd4", hovering_color = "White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Todesart = 0
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def restart():
    Fail.play()
    pygame.display.set_caption("Restart")
    
    while True:
        screen.blit(BG, (0, 0))
        
        DEATH_MOUSE_POS = pygame.mouse.get_pos()
        DEATH_TEXT = get_font(50).render("You DIED", True, "#b68f40")
        DEATH_RECT = DEATH_TEXT.get_rect(center = (300, 75))
        if Todesart == 1: #cant see
            MEME_RECT = meme_cant_see.get_rect(center = (300, 300))
            screen.blit(meme_cant_see, MEME_RECT)
        if Todesart == 2:
            MEME_RECT = meme_suicide.get_rect(center = (300, 300))
            screen.blit(meme_suicide, MEME_RECT)
        
        RESTART_BUTTON = Button(image = pygame.image.load("Hintergrund/Restart Rect.png"), pos = (100, 550), 
                            text_input = "RESTART", font = get_font(20), base_color="#d7fcd4", hovering_color = "White")
        MAIN_MENU_BUTTON = Button(image = pygame.image.load("Hintergrund/Main Menu.png"), pos = (300, 550), 
                            text_input = "MAIN MENU", font = get_font(20), base_color="#d7fcd4", hovering_color = "White")
        QUIT_BUTTON = Button(image = pygame.image.load("Hintergrund/Restart Rect.png"), pos = (500, 550), 
                            text_input = "QUIT", font = get_font(20), base_color="#d7fcd4", hovering_color = "White")
        
        screen.blit(DEATH_TEXT, DEATH_RECT)
        for button in [RESTART_BUTTON, MAIN_MENU_BUTTON, QUIT_BUTTON]:
            button.changeColor(DEATH_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                if RESTART_BUTTON.checkForInput(DEATH_MOUSE_POS) or event.key == pygame.K_SPACE:
                    play()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MAIN_MENU_BUTTON.checkForInput(DEATH_MOUSE_POS):
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
                if QUIT_BUTTON.checkForInput(DEATH_MOUSE_POS) or event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
    
        pygame.display.update()

#Äußere Gegebenheiten
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
Zellengroesse = 40   
Anzahl_Zellen = 15
screen = pygame.display.set_mode((Zellengroesse*Anzahl_Zellen,Zellengroesse*Anzahl_Zellen)) #Legt fenstergröße fest Breite*Höhe
clock = pygame.time.Clock()
FPS = 60
Todesart = 0

#Laden von ressourcen
SCHRIFTART = pygame.font.Font('Fonts/font.ttf', 25)
meme_suicide = pygame.image.load('Memes\eating ys.jpg')
meme_cant_see = pygame.image.load('Memes\cant see.jpg')
komische_frucht = pygame.image.load('Frucht\Pilz.png').convert_alpha() #convert: ändert Bild in besseres Format für python
Fail = pygame.mixer.Sound('Sounds\Fail.mp3')

#Geschwindigkeit Schlange
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()

main_menu() #Start mit dem Main Menu


