import pygame, sys, random, shelve
from pygame.math import Vector2
from button import Button
pygame.init()


programIcon = pygame.image.load("Körper_Schlange\Snake_Symbol.PNG")
pygame.display.set_icon(programIcon)

pygame.display.set_caption("Projekt: Snake")


class Schlange:
    def __init__(self):
        self.body = [Vector2(5,9),Vector2(4,9),Vector2(3,9)] #Kreiert Schlangenkörper
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
        self.Körper_rechts = pygame.image.load('Körper_Schlange\Korper_rechts.png').convert_alpha()
        self.Körper_unten = pygame.image.load('Körper_Schlange\Korper_unten.png').convert_alpha()
        self.Körper_oben = pygame.image.load('Körper_Schlange\Korper_oben.png').convert_alpha()

        self.Blau_Kopf_links = pygame.image.load('Körper_Schlange\head_left.png').convert_alpha()        #kreiert die Kopfanimation
        self.Blau_Kopf_rechts = pygame.image.load('Körper_Schlange\head_right.png').convert_alpha()
        self.Blau_Kopf_oben = pygame.image.load('Körper_Schlange\head_down.png').convert_alpha()
        self.Blau_Kopf_unten = pygame.image.load('Körper_Schlange\head_up.png').convert_alpha()

        self.Blau_Körper_LO = pygame.image.load('Körper_Schlange\\body_bottomright.png').convert_alpha()                 # kreiert die Körperanimation
        self.Blau_Körper_RO = pygame.image.load('Körper_Schlange\\body_bottomleft.png').convert_alpha()
        self.Blau_Körper_LU = pygame.image.load('Körper_Schlange\\body_topright.png').convert_alpha()
        self.Blau_Körper_RU = pygame.image.load('Körper_Schlange\\body_topleft.png').convert_alpha()

        self.Blau_Schwanz_rechts = pygame.image.load('Körper_Schlange\\tail_right.png').convert_alpha()  # kreiert die Schwanzanimation
        self.Blau_Schwanz_links = pygame.image.load('Körper_Schlange\\tail_left.png').convert_alpha()
        self.Blau_Schwanz_unten = pygame.image.load('Körper_Schlange\\tail_up.png').convert_alpha()
        self.Blau_Schwanz_oben = pygame.image.load('Körper_Schlange\\tail_down.png').convert_alpha()

        self.Blau_Körper_links = pygame.image.load('Körper_Schlange\\body_horizontal.png').convert_alpha()    # kreiert die Körperanimation
        self.Blau_Körper_rechts = pygame.image.load('Körper_Schlange\\body_horizontal.png').convert_alpha()
        self.Blau_Körper_unten = pygame.image.load('Körper_Schlange\\body_vertical.png').convert_alpha()
        self.Blau_Körper_oben = pygame.image.load('Körper_Schlange\\body_vertical.png').convert_alpha()

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
                
                if Farbe == 'Grün':
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
                if Farbe == 'Blau':
                    if vorgänger.x == folgender.x:
                        screen.blit(self.Blau_Körper_oben,Körperteil_rect) #macht bei hortizontal nur Körper unten
                    elif vorgänger.y == folgender.y:
                        screen.blit(self.Blau_Körper_rechts,Körperteil_rect) #macht bei vertikal nur Körper unten
                    else: #Ecken, wie hängen benachbarte Körperteile von dem Aktuellen ab
                        if vorgänger.x == -1 and folgender.y == -1 or vorgänger.y == -1 and folgender.x == -1:
                            screen.blit(self.Blau_Körper_RU, Körperteil_rect)
                        elif vorgänger.x == -1 and folgender.y == 1 or vorgänger.y == 1 and folgender.x == -1:
                            screen.blit(self.Blau_Körper_RO, Körperteil_rect)
                        elif vorgänger.x == 1 and folgender.y == 1 or vorgänger.y == 1 and folgender.x == 1:
                            screen.blit(self.Blau_Körper_LO, Körperteil_rect)
                        elif vorgänger.x == 1 and folgender.y == -1 or vorgänger.y == -1 and folgender.x == 1:
                            screen.blit(self.Blau_Körper_LU, Körperteil_rect)

        
    def update_Kopf_Grafiken(self):
        Kopf_abhängigkeiten = self.body[1] -self.body[0] #Findet heraus, wie sich der Kopf zum letzten Körperteil bewegt
        if Farbe == 'Grün':
            if Kopf_abhängigkeiten == Vector2(1,0):
                self.Kopf = self.Kopf_links
            elif Kopf_abhängigkeiten == Vector2(-1,0):
                self.Kopf = self.Kopf_rechts
            elif Kopf_abhängigkeiten == Vector2(0,-1):
                self.Kopf = self.Kopf_oben
            elif Kopf_abhängigkeiten == Vector2(0,1):
                self.Kopf = self.Kopf_unten
        
        if Farbe == 'Blau':
            if Kopf_abhängigkeiten == Vector2(1,0):
                self.Kopf = self.Blau_Kopf_links
            elif Kopf_abhängigkeiten == Vector2(-1,0):
                self.Kopf = self.Blau_Kopf_rechts
            elif Kopf_abhängigkeiten == Vector2(0,-1):
                self.Kopf = self.Blau_Kopf_oben
            elif Kopf_abhängigkeiten == Vector2(0,1):
                self.Kopf = self.Blau_Kopf_unten  

    def update_Schwanz_Grafiken(self):
        Schwanz_abhängigkeiten = self.body[-2] -self.body[-1] #Findet heraus, wie sich der Kopf zum letzten Körperteil bewegt
        if Farbe == 'Grün':
            if Schwanz_abhängigkeiten == Vector2(1,0):
                self.Schwanz = self.Schwanz_links
            elif Schwanz_abhängigkeiten == Vector2(-1,0):
                self.Schwanz = self.Schwanz_rechts
            elif Schwanz_abhängigkeiten == Vector2(0,-1):
                self.Schwanz = self.Schwanz_oben
            elif Schwanz_abhängigkeiten == Vector2(0,1):
                self.Schwanz = self.Schwanz_unten

        if Farbe == 'Blau':
            if Schwanz_abhängigkeiten == Vector2(1,0):
                self.Schwanz = self.Blau_Schwanz_links
            elif Schwanz_abhängigkeiten == Vector2(-1,0):
                self.Schwanz = self.Blau_Schwanz_rechts
            elif Schwanz_abhängigkeiten == Vector2(0,-1):
                self.Schwanz = self.Blau_Schwanz_oben
            elif Schwanz_abhängigkeiten == Vector2(0,1):
                self.Schwanz = self.Blau_Schwanz_unten

    def Schlange_verlängern(self):
        self.Verlängerung = True
    
    def play_sound(self):
        self.oneup.play()

    def reset(self):
        self.body = [Vector2(5,9),Vector2(4,9),Vector2(3,9)] 
        self.Richtung = Vector2(0,0)

            
class Frucht: 
    def __init__(self):
        self.Fruchtliste = [Vector2(random.randint(2, Anzahl_Zellen - 1),random.randint(2, Anzahl_Zellen - 1))]
        self.random_fruit()
        
    def Frucht_malen(self):
        
        frucht_rect = pygame.Rect(int(self.Fruchtliste[-2].x * Zellengroesse), int(self.Fruchtliste[-2].y * Zellengroesse), Zellengroesse, Zellengroesse) #!!! Rect wird großgeschrieben
        screen.blit(komische_frucht,frucht_rect)

    def random_fruit(self):
            while True:
                self.x = random.randint(2, Anzahl_Zellen - 1)
                self.y = random.randint(2, Anzahl_Zellen - 1)
                self.vor_fruchtpos = Vector2(self.x,self.y)   
                if self.vor_fruchtpos in Hindernisliste:
                    continue
                else: 
                    self.fruchtpos = self.vor_fruchtpos
                    self.Fruchtliste.append(self.fruchtpos)
                    return

class Hindernisse:
    def __init__(self):

        self.Hindernisliste = []
        self.Hindernis_Sprites = []
        self.schlange = Schlange()
        self.frucht = Frucht()
        self.random_hindernisse() 

    def Hindernisse_malen(self):
        if Level ==2 :
            i = 0 
            for hindernis in self.Hindernisliste:
                self.Hindernis_Sprites.append(random.choice([Cactus_1, Cactus_2, Cactus_3, Cactus_4]))
                hindernis_rect = pygame.Rect(int(hindernis.x * Zellengroesse), int(hindernis.y * Zellengroesse), Zellengroesse, Zellengroesse) #!!! Rect wird großgeschrieben
                screen.blit(self.Hindernis_Sprites[i],hindernis_rect)
                i += 1
        
    
    def random_hindernisse(self):
        if Level == 2:
            while True:
                self.x = random.randint(2, Anzahl_Zellen - 1)
                self.y = random.randint(2, Anzahl_Zellen - 1)
                self.pos = Vector2(self.x,self.y)
                if self.pos in self.schlange.body or self.pos == self.frucht.Fruchtliste[-1] or self.pos in self.Hindernisliste: #Wenn hindernisse in Schlange nochamal oder in Frucht
                    continue
                else: 
                    self.securepos = self.pos
                    self.Hindernisliste.append(self.securepos)
                    return
    
    def reset(self):
        global Hindernisliste
        if Todesart != 0:
            self.Hindernisliste = []
            self.random_hindernisse()

class MAIN:
    def __init__(self):
        self.schlange = Schlange()
        self.frucht = Frucht ()
        self.hindernisse = Hindernisse()

    def Update(self):
        self.schlange.Schlange_bewegen()
        self.Kollisionen()
        self.Tod()
        self.check_fail()
  
    def Malen(self):
        self.Gras_Feld()
        self.Score()
        self.Highscore()
        main_game.frucht.Frucht_malen()
        main_game.hindernisse.Hindernisse_malen()
        main_game.schlange.Schlange_malen()
        
        
    def Kollisionen(self):
        if self.frucht.Fruchtliste[-2] == self.schlange.body[0]:
            self.frucht.random_fruit()
            self.schlange.Schlange_verlängern()
            self.schlange.play_sound()
            self.hindernisse.random_hindernisse()
        
        
        for Körperteil in self.schlange.body[1:]: #Wenn Frucht Position in Körper der Schlange, dann erneut random
            if Körperteil == self.frucht.Fruchtliste[-2]: 
                self.frucht.random_fruit()
        
        if Level == 2:
            for Körperteil in self.schlange.body[1:]:
                if Körperteil == self.hindernisse.securepos or self.hindernisse.securepos == (self.schlange.body[0] + self.schlange.Richtung):
                    del self.hindernisse.Hindernisliste[-1]
                    self.hindernisse.random_hindernisse()
        
            if self.frucht.Fruchtliste[-2] in self.hindernisse.Hindernisliste:
                self.frucht.random_fruit()                            
                
    def check_fail(self): # Schlange trifft sich selbst oder rand, Spiel wird beendet
        global safe_score1, safe_score2, hindernis, Level

        if not 2 <= self.schlange.body[0].x < Anzahl_Zellen + 2 or not 2 <= self.schlange.body[0].y < Anzahl_Zellen +2:
            if Level == 1:
                safe_score1 = str(len(self.schlange.body) - 3)
            elif Level == 2:
                safe_score2 = str(len(self.schlange.body) - 3)
            self.hindernisse.reset()
            self.game_over()

        if Level == 2:
            for hindernis in self.hindernisse.Hindernisliste:
                if hindernis == self.schlange.body[0]:
                    safe_score2 = str(len(self.schlange.body) - 3)
                    self.hindernisse.reset()
                    self.game_over()
            
        for Körperteil in self.schlange.body[1:]:
            if Körperteil == self.schlange.body[0]:
                if Level == 1:
                    safe_score1 = str(len(self.schlange.body) - 3)
                if Level == 2:
                    safe_score2 = str(len(self.schlange.body) - 3)
                self.hindernisse.reset()
                self.game_over()
                 

    def Tod(self): # Schlange trifft sich selbst oder rand, Spiel wird beendet
        global Todesart   
        if not 2 <= self.schlange.body[0].x < Anzahl_Zellen + 2 or not 2 <= self.schlange.body[0].y < Anzahl_Zellen +2 : #Wenn nicht im feld
            Todesart = 1
        
        for Körperteil in self.schlange.body[1:]:
            if Körperteil == self.schlange.body[0] and not self.schlange.body[0] == Vector2(5, 9) and not self.schlange.body[1] == Vector2(4, 9) and not self.schlange.body[2] == Vector2(3,9):
                Todesart = 2
        
        
        if Level == 2:
            for hindernis in self.hindernisse.Hindernisliste:
                if hindernis == self.schlange.body[0]:
                    Todesart = 3


    def game_over(self):
        self.schlange.reset()

    def Gras_Feld(self):
    
        GRAS_FARBE = (240,230,140) # #159,24,18 
        for Zeile in range(Anzahl_Zellen):
            if Zeile % 2 == 0:
                for Zelle in range(Anzahl_Zellen):
                    if Zelle % 2 == 0:
                        grass_rect = pygame.Rect(Zelle * Zellengroesse + Overlay_bar, Zeile * Zellengroesse + Overlay_bar, Zellengroesse, Zellengroesse)
                        pygame.draw.rect(screen,GRAS_FARBE,grass_rect)
            else:
                for Zelle in range(Anzahl_Zellen):
                    if Zelle % 2 != 0:
                        grass_rect = pygame.Rect(Zelle * Zellengroesse + Overlay_bar, Zeile * Zellengroesse + Overlay_bar, Zellengroesse, Zellengroesse)
                        pygame.draw.rect(screen,GRAS_FARBE,grass_rect)

    def Score(self):
        global current_score
        current_score = str(len(self.schlange.body) - 3) #score startet nicht bei 3
        score_surface = SCHRIFTART.render(current_score, True, (56,74,12))
        score_x = int(340) #Wo Score Anzeige
        score_y = int(40)
        score_rect = score_surface.get_rect(center = (score_x,score_y)) #Macht ein rectangle um den Score, und platziert mittif davon
        frucht_rect = komische_frucht.get_rect(midright = (score_rect.left, score_rect.centery))

        screen.blit(score_surface, score_rect)
        screen.blit(komische_frucht, frucht_rect)
        return current_score

    def Highscore(self):
        global safe_score1, Highscore1, safe_score2, Highscore2, Level, loading_states, Sterne_lvl_1, Sterne_lvl_2

        if Level == 1:

            Highscore = Highscore1
            trophy = silver_trophy
            if int(safe_score1) > int(Highscore1) and Todesart != 0:
                Highscore1 = safe_score1
                d = shelve.open('score.txt')  # here you will save the score variable   
                d['Highscore1'] = Highscore1  
                d.close()
                
        if Level == 2:
            trophy = gold_trophy
            Highscore = Highscore2
            if int(safe_score2) > int(Highscore2) and Todesart != 0:
                    Highscore2 = safe_score2
                    d = shelve.open('score.txt')  # here you will save the score variable   
                    d['Highscore2'] = Highscore2           # thats all, now it is saved on disk.
                    d.close()


        highscore_surface = SCHRIFTART.render(Highscore, True, (56,74,12))
        highscore_x = int(440) #Wo Score Anzeige
        highscore_y = int(40)

        highscore_rect = highscore_surface.get_rect(center = (highscore_x,highscore_y)) #Macht ein rectangle um den Score, und platziert mittif davon
        trophy_rect = silver_trophy.get_rect(midright = (highscore_rect.left, highscore_rect.centery))
        screen.blit(highscore_surface, highscore_rect)
        screen.blit(trophy, trophy_rect)



    def Levelwahl(self):
        if Level == 1:
            self.frucht.Fruchtliste = []
        elif Level == 2:
            self.hindernisse.random_hindernisse()
        

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Fonts/font.ttf", size)

def play():
    pygame.display.set_caption("Play")
    global Todesart, es_score
    Todesart = 0
    spielen = True
    while spielen: #Game loop
        es_score = str(len(main_game.schlange.body) - 3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Kontrolliert ob auf das x gedrückt wurde
                pygame.quit() #Fenster schließen
                sys.exit() #beendet allen Code
            if event.type == SCREEN_UPDATE:
                main_game.Update()
                
            if event.type == pygame.KEYDOWN:
                
                if main_game.schlange.Richtung == Vector2(0,0):
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        main_game.schlange.Richtung = Vector2(1, 0)
                    
                elif event.key == pygame.K_UP or event.key == pygame.K_w: #Steuerung
                    if main_game.schlange.Richtung.y != 1: #Man kann nur nach oben gehen, wenn man nicht nach unten geht
                        main_game.schlange.Richtung = Vector2(0, -1)

                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if main_game.schlange.Richtung.y != -1:
                        main_game.schlange.Richtung = Vector2(0, 1)

                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if main_game.schlange.Richtung.x != 1:
                        main_game.schlange.Richtung = Vector2(-1, 0)
                    
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if main_game.schlange.Richtung.x != -1:
                        main_game.schlange.Richtung = Vector2(1, 0)
        
        if Level == 1:
            screen.blit(Wüste_BG, (0,0))
        if Level == 2:
            screen.blit(Wüste_BG_2, (0,0))
        Feldrahmen_rect = pygame.Rect(75,75,610,610)        
        pygame.draw.rect(screen, (79, 70, 65), Feldrahmen_rect, 0) #((205,198,115),Feld_rect)
        Feld_rect = pygame.Rect(80,80,600,600)
        pygame.draw.rect(screen, (205,198,115), Feld_rect, 0) #((205,198,115),Feld_rect)
        

        main_game.Malen()
        pygame.display.update() #Updatet nach jedem while loop
        clock.tick(FPS) #updatet 30x pro sekunde
        if Todesart != 0:
            spielen = False
            restart()  
            main_game.Highscore()
             


def main_menu():
    pygame.display.set_caption("Main Menu")
    global Todesart, Highscore1, Highscore2, loading_states, Sterne_lvl_2, Sterne_lvl_1

    while True:
        if loading_states:
            d = shelve.open('score.txt')
            if 'Highscore1' in d:
                Highscore1 = d['Highscore1']
            else: Highscore1 = str(0)
            if 'Highscore2' in d:  
                Highscore2 = d['Highscore2']
            else: Highscore2 = str(0)
            if 'Sterne_lvl_1' in d:
                Sterne_lvl_1 = d['Sterne_lvl_1']
            else: Sterne_lvl_1 = 0
            if 'Sterne_lvl_2' in d:  
                Sterne_lvl_2 = d['Sterne_lvl_2']
            else: Sterne_lvl_2 = 0
            d.close()
            loading_states = False
            
        if Level == 1:
            screen.blit(Wüste_BG, (0,0))
        if Level == 2:
            screen.blit(Wüste_BG_2, (0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(50).render("SNAKE GAME", True, (56,74,12))
        MENU_RECT = MENU_TEXT.get_rect(center = (380, 100))

        PLAY_BUTTON = Button(image = pygame.image.load("Hintergrund/Options Rect.png"), pos = (380, 250), 
                            text_input = "Play", font = get_font(50), base_color="#d7fcd4", hovering_color = "White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Hintergrund/Options Rect.png"), pos=(380, 375), 
                            text_input="Options", font = get_font(50), base_color="#d7fcd4", hovering_color = "White")
        QUIT_BUTTON = Button(image = pygame.image.load("Hintergrund/Options Rect.png"), pos = (380, 500), 
                            text_input = "Quit", font = get_font(50), base_color="#d7fcd4", hovering_color = "White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Todesart = 0
                    button_sound.play()
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    button_sound.play()
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    button_sound.play()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def options():
    pygame.display.set_caption("Options")
    
    while True:
        screen.blit(Wüste_BG_3, (0, 0))
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        OPTIONS_TEXT = get_font(50).render("OPTIONS", True, "#b68f40")  
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center = (380, 75))
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()        

        LEVEL_BUTTON = Button(image = pygame.image.load("Hintergrund/Options Rect.png"), pos = (380, 200), 
                            text_input = "Level", font = get_font(50), base_color="#d7fcd4", hovering_color = "White")        
        SKIN_BUTTON = Button(image = pygame.image.load("Hintergrund/Options Rect.png"), pos = (380, 325), 
                            text_input = "Skins", font = get_font(50), base_color="#d7fcd4", hovering_color = "White")
        RESET_BUTTON = Button(image = pygame.image.load("Hintergrund/Options Rect.png"), pos = (380, 450), 
                            text_input = "Reset", font = get_font(50), base_color="#d7fcd4", hovering_color = "White")
        MAIN_MENU_BUTTON = Button(image = pygame.image.load("Hintergrund/Options Rect.png"), pos = (380, 575), 
                    text_input = "Back", font = get_font(50), base_color="#d7fcd4", hovering_color = "White")

        for button in [MAIN_MENU_BUTTON, LEVEL_BUTTON, SKIN_BUTTON, RESET_BUTTON]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(screen)

        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MAIN_MENU_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    button_sound.play()
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SKIN_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    button_sound.play()
                    skins()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    button_sound.play()
                    level()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESET_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    button_sound.play()
                    reset_highscore()

        pygame.display.update()  
        
def reset_highscore():
    global Highscore2, Highscore1, Sterne_lvl_1, Sterne_lvl_2
    Highscore1 = str(0)
    Highscore2 = str(0)
    Sterne_lvl_1 = 0
    Sterne_lvl_2 = 0
    d = shelve.open('score.txt')
    d.clear()  
    d.close()


def skins():
    global Farbe
    pygame.display.set_caption("Skins")
    
    while True:  
        screen.blit(Wüste_BG_3, (0, 0))
        SKIN_MOUSE_POS = pygame.mouse.get_pos()
        SKIN_TEXT = get_font(50).render("SKIN WAHL", True, "#b68f40")
        SKIN_RECT = SKIN_TEXT.get_rect(center = (380, 75))
        SKIN_MOUSE_POS = pygame.mouse.get_pos()

        blaue_Schlange_rect = blau_ganze_Schlange.get_rect(center = (230, 330))
        screen.blit(blau_ganze_Schlange, blaue_Schlange_rect)
        if Farbe == 'Blau':
            haekchen_blau_rect = haekchen.get_rect(center = (310, 385))
            screen.blit(haekchen, haekchen_blau_rect)

        gruene_ganze_Schlange_rect = grun_ganze_Schlange.get_rect(center = (530, 330))
        screen.blit(grun_ganze_Schlange, gruene_ganze_Schlange_rect)
        if Farbe == 'Grün': 
            haekchen_gruen_rect = haekchen.get_rect(center = (610, 385))
            screen.blit(haekchen, haekchen_gruen_rect)

        SKIN_BUTTON = Button(image = pygame.image.load("Hintergrund/Restart Rect.png"), pos = (230, 480), 
                            text_input = "Blau", font = get_font(20), base_color="#d7fcd4", hovering_color = "White")
        SKIN_BUTTON_2 = Button(image = pygame.image.load("Hintergrund/Restart Rect.png"), pos = (530, 480), 
                            text_input = "Grün", font = get_font(20), base_color="#d7fcd4", hovering_color = "White")
        MAIN_MENU_BUTTON = Button(image = pygame.image.load("Hintergrund/Restart Rect.png"), pos = (380, 600), 
                            text_input = "Back", font = get_font(20), base_color="#d7fcd4", hovering_color = "White")

        screen.blit(SKIN_TEXT, SKIN_RECT)
        for button in [SKIN_BUTTON, SKIN_BUTTON_2, MAIN_MENU_BUTTON]:
            button.changeColor(SKIN_MOUSE_POS)
            button.update(screen) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SKIN_BUTTON.checkForInput(SKIN_MOUSE_POS):
                    button_sound.play()
                    Farbe = 'Blau'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SKIN_BUTTON_2.checkForInput(SKIN_MOUSE_POS):
                    button_sound.play()
                    Farbe = 'Grün'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MAIN_MENU_BUTTON.checkForInput(SKIN_MOUSE_POS):
                    button_sound.play()
                    options()                    
        
        pygame.display.update() 


def level():
    global Level, loading_states, Sterne_lvl_1, Sterne_lvl_2
    pygame.display.set_caption("Level")
    
    while True:  
            
        screen.blit(Wüste_BG_3, (0, 0))
        LEVEL_MOUSE_POS = pygame.mouse.get_pos()
        LEVEL_TEXT = get_font(50).render("LEVEL WAHL", True, "#b68f40")
        LEVEL_RECT = LEVEL_TEXT.get_rect(center = (380, 75))
        LEVEL_MOUSE_POS = pygame.mouse.get_pos()

        if Sterne_lvl_1 == 0:
            Stern1_links_rect = star_50.get_rect(center = (170,215)) #Stern links
            screen.blit(star_50_grey,Stern1_links_rect)
            Stern1_rechts_rect = star_50.get_rect(center = (290,215)) #Stern rechts
            screen.blit(star_50_grey,Stern1_rechts_rect)
            Stern1_mitte_rect = star_80.get_rect(center = (230,200)) #Stern Mitte
            screen.blit(star_80_grey,Stern1_mitte_rect)

        elif Sterne_lvl_1 == 1:
            Stern1_links_rect = star_50.get_rect(center = (170,215))
            screen.blit(star_50,Stern1_links_rect)
            Stern1_rechts_rect = star_50.get_rect(center = (290,215))
            screen.blit(star_50_grey,Stern1_rechts_rect)
            Stern1_mitte_rect = star_80.get_rect(center = (230,200))
            screen.blit(star_80_grey,Stern1_mitte_rect)

        elif Sterne_lvl_1 == 2:
            Stern1_links_rect = star_50.get_rect(center = (170,215))
            screen.blit(star_50,Stern1_links_rect)
            Stern1_rechts_rect = star_50.get_rect(center = (290,215))
            screen.blit(star_50,Stern1_rechts_rect)
            Stern1_mitte_rect = star_80.get_rect(center = (230,200))
            screen.blit(star_80_grey,Stern1_mitte_rect)

        elif Sterne_lvl_1 == 3:
            Stern1_links_rect = star_50.get_rect(center = (170,215))
            screen.blit(star_50,Stern1_links_rect)
            Stern1_rechts_rect = star_50.get_rect(center = (290,215))
            screen.blit(star_50,Stern1_rechts_rect)
            Stern1_mitte_rect = star_80.get_rect(center = (230,200))
            screen.blit(star_80,Stern1_mitte_rect)

        if Sterne_lvl_2 == 0:
            Stern2_links_rect = star_50.get_rect(center = (470,215)) #Stern links
            screen.blit(star_50_grey,Stern2_links_rect)
            Stern2_rechts_rect = star_50.get_rect(center = (590,215)) #Stern rechts
            screen.blit(star_50_grey,Stern2_rechts_rect)
            Stern2_mitte_rect = star_80.get_rect(center = (530,200)) #Stern Mitte
            screen.blit(star_80_grey,Stern2_mitte_rect)

        elif Sterne_lvl_2 == 1:
            Stern2_links_rect = star_50.get_rect(center = (470,215))
            screen.blit(star_50,Stern2_links_rect)
            Stern2_rechts_rect = star_50.get_rect(center = (590,215))
            screen.blit(star_50_grey,Stern2_rechts_rect)
            Stern2_mitte_rect = star_80.get_rect(center = (530,200))
            screen.blit(star_80_grey,Stern2_mitte_rect)

        elif Sterne_lvl_2 == 2:
            Stern2_links_rect = star_50.get_rect(center = (470,215))
            screen.blit(star_50,Stern2_links_rect)
            Stern2_rechts_rect = star_50.get_rect(center = (590,215))
            screen.blit(star_50,Stern2_rechts_rect)
            Stern2_mitte_rect = star_80.get_rect(center = (530,200))
            screen.blit(star_80_grey,Stern2_mitte_rect)
            
        elif Sterne_lvl_2 == 3:
            Stern2_links_rect = star_50.get_rect(center = (470,215))
            screen.blit(star_50,Stern2_links_rect)
            Stern2_rechts_rect = star_50.get_rect(center = (590,215))
            screen.blit(star_50,Stern2_rechts_rect)
            Stern2_mitte_rect = star_80.get_rect(center = (530,200))
            screen.blit(star_80,Stern2_mitte_rect)


        level1_rect = level_1.get_rect(center = (230, 330))
        screen.blit(level_1, level1_rect)
        if Level == 1:
            haekchen_level1_rect = haekchen.get_rect(center = (340, 410))
            screen.blit(haekchen, haekchen_level1_rect)

        level2_rect = level_2.get_rect(center = (530, 330))
        screen.blit(level_2, level2_rect)
        if Level == 2:
            haekchen_level2_rect = haekchen.get_rect(center = (640, 410))
            screen.blit(haekchen, haekchen_level2_rect)
        
     
        LEVEL_BUTTON = Button(image = pygame.image.load("Hintergrund/Restart Rect.png"), pos = (230, 480), 
                            text_input = "Level 1", font = get_font(20), base_color="#d7fcd4", hovering_color = "White")
        LEVEL_BUTTON_2 = Button(image = pygame.image.load("Hintergrund/Restart Rect.png"), pos = (530, 480), 
                            text_input = "Level 2", font = get_font(20), base_color="#d7fcd4", hovering_color = "White")
        MAIN_MENU_BUTTON = Button(image = pygame.image.load("Hintergrund/Restart Rect.png"), pos = (380, 600), 
                            text_input = "Back", font = get_font(20), base_color="#d7fcd4", hovering_color = "White")

        screen.blit(LEVEL_TEXT, LEVEL_RECT)
        for button in [LEVEL_BUTTON, LEVEL_BUTTON_2, MAIN_MENU_BUTTON]:
            button.changeColor(LEVEL_MOUSE_POS)
            button.update(screen) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MAIN_MENU_BUTTON.checkForInput(LEVEL_MOUSE_POS):
                    button_sound.play()
                    options() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL_BUTTON.checkForInput(LEVEL_MOUSE_POS):
                    button_sound.play()
                    Level = 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL_BUTTON_2.checkForInput(LEVEL_MOUSE_POS):
                    button_sound.play()
                    Level = 2
                    main_game.hindernisse.random_hindernisse()
                
        pygame.display.update() 


def restart():
    global es_score, Sterne_lvl_1, Sterne_lvl_2
    Fail.play()
    pygame.display.set_caption("Exit Menu")
    
    while True:

        if Level == 1:
            Anzahl_Sterne_1 = int(int(es_score)/10)
            screen.blit(Wüste_BG, (0,0))
            if Sterne_lvl_1 == 0:
                if Anzahl_Sterne_1 == 0:
                    Sterne_zahl_Text = get_font(20).render(f'You need {10-int(es_score)} points more for 1 star', True, (56,74,12))
                    Sterne_zahl_Rect = Sterne_zahl_Text.get_rect(center = (380, 160))
                if Anzahl_Sterne_1 == 1:
                    Sterne_zahl_Text = get_font(20).render(f'You got your second Star(s)', True, (56,74,12))
                    Sterne_zahl_Rect = Sterne_zahl_Text.get_rect(center = (380, 160))
                    Sterne_lvl_1 = Anzahl_Sterne_1
                elif Anzahl_Sterne_1 == 2:
                    Sterne_zahl_Text = get_font(20).render(f'You got your second Star', True, (56,74,12))
                    Sterne_zahl_Rect = Sterne_zahl_Text.get_rect(center = (380, 160))
                    Sterne_lvl_1 = 2
                elif Anzahl_Sterne_1 >= 3:
                    Sterne_zahl_Text = get_font(20).render(f'You got all 3 Star(s). Congratulations', True, (56,74,12))
                    Sterne_zahl_Rect = Sterne_zahl_Text.get_rect(center = (380, 160))
                    Sterne_lvl_1 = 3
                
                d = shelve.open('score.txt')  #Abspeichern in datei
                d['Sterne_lvl_1'] = Sterne_lvl_1           
                d.close()
                
            elif Sterne_lvl_1 == 1:
                
                if Anzahl_Sterne_1 <= 1:
                    Sterne_zahl_Text = get_font(20).render(f'You need {20-int(es_score)} points more for 2 stars', True, (56,74,12))
                    Sterne_zahl_Rect = Sterne_zahl_Text.get_rect(center = (380, 160))

                elif Anzahl_Sterne_1 == 2:
                    Sterne_zahl_Text = get_font(20).render(f'You got your second Star', True, (56,74,12))
                    Sterne_zahl_Rect = Sterne_zahl_Text.get_rect(center = (380, 160))
                    Sterne_lvl_1 = 2
                elif Anzahl_Sterne_1 >= 3:
                    Sterne_zahl_Text = get_font(20).render(f'You got all 3 Star(s). Congratulations', True, (56,74,12))
                    Sterne_zahl_Rect = Sterne_zahl_Text.get_rect(center = (380, 160))
                    Sterne_lvl_1 = 3
                
                d = shelve.open('score.txt') 
                d['Sterne_lvl_1'] = Sterne_lvl_1           
                d.close()
                
            elif Sterne_lvl_1 >= 2:
                if Anzahl_Sterne_1 < 3:
                    Sterne_zahl_Text = get_font(20).render(f'You need {30-int(es_score)} points more for 3 stars', True, (56,74,12))
                    Sterne_zahl_Rect = Sterne_zahl_Text.get_rect(center = (380, 160))
                if Anzahl_Sterne_1 > 2:
                    Sterne_zahl_Text = get_font(20).render(f'You got all 3 Star(s)', True, (56,74,12))
                    Sterne_zahl_Rect = Sterne_zahl_Text.get_rect(center = (380, 160))
                    Sterne_lvl_1 = 3
                
                d = shelve.open('score.txt') 
                d['Sterne_lvl_1'] = Sterne_lvl_1           
                d.close()

        if Level == 2:
            Anzahl_Sterne_2 = int(int(es_score)/10)
            screen.blit(Wüste_BG_2, (0,0))
            
            if Sterne_lvl_2 == 0:
                if Anzahl_Sterne_2 == 0:
                    Sterne_zahl_Text = get_font(20).render(f'You need {10-int(es_score)} points more for 1 star', True, (56,74,12))
                    Sterne_zahl_Rect = Sterne_zahl_Text.get_rect(center = (380, 160))
                if Anzahl_Sterne_2 == 1:
                    Sterne_zahl_Text = get_font(20).render(f'You got your first Star(s)', True, (56,74,12))
                    Sterne_zahl_Rect = Sterne_zahl_Text.get_rect(center = (380, 160))
                    Sterne_lvl_2 = Anzahl_Sterne_2
                elif Anzahl_Sterne_2 == 2:
                    Sterne_zahl_Text = get_font(20).render(f'You got your second Star', True, (56,74,12))
                    Sterne_zahl_Rect = Sterne_zahl_Text.get_rect(center = (380, 160))
                    Sterne_lvl_2 = 2
                elif Anzahl_Sterne_2 >= 3:
                    Sterne_zahl_Text = get_font(20).render(f'You got all 3 Star(s). Congratulations', True, (56,74,12))
                    Sterne_zahl_Rect = Sterne_zahl_Text.get_rect(center = (380, 160))
                    Sterne_lvl_2 = 3
                
                d = shelve.open('score.txt') 
                d['Sterne_lvl_2'] = Sterne_lvl_2           
                d.close()
                
            elif Sterne_lvl_2 == 1:
                if Anzahl_Sterne_2 <= 1:
                    Sterne_zahl_Text = get_font(20).render(f'You need {20-int(es_score)} points more for 2 stars', True, (56,74,12))
                    Sterne_zahl_Rect = Sterne_zahl_Text.get_rect(center = (380, 160))

                elif Anzahl_Sterne_2 == 2:
                    Sterne_zahl_Text = get_font(20).render(f'You got your second Star', True, (56,74,12))
                    Sterne_zahl_Rect = Sterne_zahl_Text.get_rect(center = (380, 160))
                    Sterne_lvl_2 = 2
                elif Anzahl_Sterne_2 >= 3:
                    Sterne_zahl_Text = get_font(20).render(f'You got all 3 Star(s). Congratulations', True, (56,74,12))
                    Sterne_zahl_Rect = Sterne_zahl_Text.get_rect(center = (380, 160))
                    Sterne_lvl_2 = 3
                
                d = shelve.open('score.txt') 
                d['Sterne_lvl_2'] = Sterne_lvl_2           
                d.close()
                
            elif Sterne_lvl_2 >= 2:
                if Anzahl_Sterne_2 < 3:
                    Sterne_zahl_Text = get_font(20).render(f'You need {30-int(es_score)} points more for 3 stars', True, (56,74,12))
                    Sterne_zahl_Rect = Sterne_zahl_Text.get_rect(center = (380, 160))
                if Anzahl_Sterne_2 > 2:
                    Sterne_zahl_Text = get_font(20).render(f'You got all 3 Star(s)', True, (56,74,12))
                    Sterne_zahl_Rect = Sterne_zahl_Text.get_rect(center = (380, 160))
                    Sterne_lvl_2 = 3  
                
                d = shelve.open('score.txt') 
                d['Sterne_lvl_2'] = Sterne_lvl_2           
                d.close()
        
        DEATH_MOUSE_POS = pygame.mouse.get_pos()
        DEATH_TEXT = get_font(50).render("You DIED", True, (56,74,12))
        DEATH_RECT = DEATH_TEXT.get_rect(center = (380, 75))
        
        STAR_TEXT = get_font(20).render(f'You achieved a score of {es_score}', True, (56,74,12))
        STAR_TEXT_RECT = STAR_TEXT.get_rect(center = (380, 120))
                

        if Todesart == 1: #cant see
            MEME_RECT = meme_cant_see.get_rect(center = (380, 415))
            screen.blit(meme_cant_see, MEME_RECT)
        if Todesart == 2:
            MEME_RECT = meme_suicide.get_rect(center = (380, 415))
            screen.blit(meme_suicide, MEME_RECT)
        if Todesart == 3: #cactus
            MEME_RECT = meme_cactus.get_rect(center = (380, 415))
            screen.blit(meme_cactus, MEME_RECT)
        
        RESTART_BUTTON = Button(image = pygame.image.load("Hintergrund/Restart Rect.png"), pos = (175, 700), 
                            text_input = "Restart", font = get_font(20), base_color = "#d7fcd4", hovering_color = "White")
        MAIN_MENU_BUTTON = Button(image = pygame.image.load("Hintergrund/Main Menu.png"), pos = (380, 700), 
                            text_input = "Main Menu", font = get_font(20), base_color = "#d7fcd4", hovering_color = "White")
        QUIT_BUTTON = Button(image = pygame.image.load("Hintergrund/Restart Rect.png"), pos = (585, 700), 
                            text_input = "Quit", font = get_font(20), base_color = "#d7fcd4", hovering_color = "White")
        
        screen.blit(DEATH_TEXT, DEATH_RECT)
        screen.blit(STAR_TEXT, STAR_TEXT_RECT)
        screen.blit(Sterne_zahl_Text, Sterne_zahl_Rect)
        for button in [RESTART_BUTTON, MAIN_MENU_BUTTON, QUIT_BUTTON]:
            button.changeColor(DEATH_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    play()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESTART_BUTTON.checkForInput(DEATH_MOUSE_POS):
                    button_sound.play()
                    play()
                if MAIN_MENU_BUTTON.checkForInput(DEATH_MOUSE_POS):
                    button_sound.play()
                    main_menu()
                if QUIT_BUTTON.checkForInput(DEATH_MOUSE_POS):
                    button_sound.play()
                    pygame.quit()
                    sys.exit()
                    
        pygame.display.update()

#Äußere Gegebenheiten
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
Zellengroesse = 40   
Anzahl_Zellen = 15
Overlay_bar = 80
Feldhöhe = Zellengroesse * Anzahl_Zellen + Overlay_bar
screen = pygame.display.set_mode((Zellengroesse*Anzahl_Zellen+2*Overlay_bar,Feldhöhe+Overlay_bar)) #Legt fenstergröße fest Breite*Höhe
clock = pygame.time.Clock()
FPS = 60
Todesart = 0
Highscore1 = str(0)
Highscore2 = str(0)
safe_score1 = str(0)
safe_score2 = str(0)
BG = pygame.image.load("Hintergrund/Background.png")

#Laden von ressourcen
SCHRIFTART = pygame.font.Font('Fonts/font.ttf', 25)
meme_suicide = pygame.image.load('Memes\eating ys.jpg').convert_alpha()
meme_cant_see = pygame.image.load('Memes\cant see.jpg').convert_alpha()
meme_cactus = pygame.image.load('Memes\cactus.jpg').convert_alpha()
komische_frucht = pygame.image.load('Sprites\Pilz.png').convert_alpha() #convert: ändert Bild in besseres Format für python
silver_trophy = pygame.image.load('Sprites/silver_trophy.png').convert_alpha()
gold_trophy = pygame.image.load('Sprites/gold_trophy.png').convert_alpha()
Cactus_1 = pygame.image.load('Sprites/cactus_1.png').convert_alpha()
Cactus_2 = pygame.image.load('Sprites/cactus_2.png').convert_alpha()
Cactus_3 = pygame.image.load('Sprites/cactus_3.png').convert_alpha()
Cactus_4 = pygame.image.load('Sprites/cactus_4.png').convert_alpha()
Fail = pygame.mixer.Sound('Sounds\Fail.mp3')
button_sound = pygame.mixer.Sound('Sounds/button.mp3')
button_sound.set_volume(0.5)
blau_ganze_Schlange =  pygame.image.load('Sprites/blau_ganze_Schlange.png').convert_alpha()
grun_ganze_Schlange = pygame.image.load('Sprites/grun_ganze_Schlange.png').convert_alpha()
haekchen = pygame.image.load('Sprites/häkchen.PNG').convert_alpha()
level_1 = pygame.image.load('Sprites/level_1.PNG').convert_alpha()
level_2 = pygame.image.load('Sprites/level_2.PNG').convert_alpha()
Wüste_BG = pygame.image.load('Hintergrund/desert.jpg').convert_alpha()
Wüste_BG_2 = pygame.image.load('Hintergrund/desert2.jpg').convert_alpha()
Wüste_BG_3 = pygame.image.load('Hintergrund/desert3.png').convert_alpha()
star_50 = pygame.image.load('Sprites/star_50.png').convert_alpha()
star_50_grey = pygame.image.load('Sprites/star_50_grey.png').convert_alpha()
star_80 = pygame.image.load('Sprites/star_80.png').convert_alpha()
star_80_grey = pygame.image.load('Sprites/star_80_grey.png').convert_alpha()


#Startoptions
Farbe = 'Blau'
Level = 1
Sterne_lvl_1 = 0
Sterne_lvl_2 = 0
es_score = 0

#Hindernisse
Start_Hindernis = Vector2(random.randint(2, Anzahl_Zellen - 1),random.randint(2, Anzahl_Zellen - 1))
Hindernisliste = []
#Geschwindigkeit Schlange
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

#save states
loading_states = True

main_game = MAIN()

main_menu() #Start mit dem Main Menu

#To-Do
#Desktop app
#3. Modus wird erst angezeig, wenn 2. auf 3 Sterne