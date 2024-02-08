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

        self.Blau_Körper_LO = pygame.image.load('Körper_Schlange\\body_bottomright.png').convert_alpha()   # kreiert die Körperanimation
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

        self.oneup = pygame.mixer.Sound('Sounds/1UP.mp3')
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
        
        frucht_rect = pygame.Rect(int(self.Fruchtliste[-2].x * Zellengroesse), int(self.Fruchtliste[-2].y * Zellengroesse), Zellengroesse, Zellengroesse) 
        screen.blit(Pilz,frucht_rect)

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
        if Level == 2 or Level == 3:
            i = 0 
            for hindernis in self.Hindernisliste:
                self.Hindernis_Sprites.append(random.choice([Cactus_1, Cactus_2, Cactus_3, Cactus_4]))
                hindernis_rect = pygame.Rect(int(hindernis.x * Zellengroesse), int(hindernis.y * Zellengroesse), Zellengroesse, Zellengroesse)
                screen.blit(self.Hindernis_Sprites[i],hindernis_rect)
                i += 1
        
    
    def random_hindernisse(self):
        if Level == 2 or Level == 3:
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

class MAIN:
    def __init__(self):
        self.schlange = Schlange()
        self.frucht = Frucht ()
        self.hindernisse = Hindernisse()
        self.silver_trophy = pygame.image.load('Sprites/silver_trophy.png').convert_alpha()
        self.gold_trophy = pygame.image.load('Sprites/gold_trophy.png').convert_alpha()
        self.rage_trophy = pygame.image.load('Sprites/mad_face.png').convert_alpha()

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
        
        if Level == 2 or Level == 3:
            for Körperteil in self.schlange.body[1:]:
                if Körperteil == self.hindernisse.securepos or self.hindernisse.securepos == (self.schlange.body[0] + self.schlange.Richtung):
                    del self.hindernisse.Hindernisliste[-1]
                    self.hindernisse.random_hindernisse()
        
            if self.frucht.Fruchtliste[-2] in self.hindernisse.Hindernisliste:
                self.frucht.random_fruit()                            
                
    def check_fail(self): # Schlange trifft sich selbst oder rand, Spiel wird beendet
        global safe_score1, safe_score2, safe_score3, hindernis, Level, Todesart

        if not 2 <= self.schlange.body[0].x < Anzahl_Zellen + 2 or not 2 <= self.schlange.body[0].y < Anzahl_Zellen +2:
            if Level == 1:
                safe_score1 = str(len(self.schlange.body) - 3)
            elif Level == 2:
                safe_score2 = str(len(self.schlange.body) - 3)
            elif Level == 3:
                safe_score3 = str(len(self.schlange.body) - 3)
            self.hindernisse.reset()
            self.schlange.reset()

        if Level == 2 :
            for hindernis in self.hindernisse.Hindernisliste:
                if hindernis == self.schlange.body[0]:
                    safe_score2 = str(len(self.schlange.body) - 3)
                    self.hindernisse.reset()
                    self.schlange.reset()
                    
        if Level == 3 :
            for hindernis in self.hindernisse.Hindernisliste:
                if hindernis == self.schlange.body[0]:
                    safe_score3 = str(len(self.schlange.body) - 3)
                    self.hindernisse.reset()
                    self.schlange.reset()

        for Körperteil in self.schlange.body[1:]:
            if Körperteil == self.schlange.body[0]:
                if Level == 1:
                    safe_score1 = str(len(self.schlange.body) - 3)
                if Level == 2:
                    safe_score2 = str(len(self.schlange.body) - 3)
                if Level == 3:
                    safe_score3 = str(len(self.schlange.body) - 3)
                self.hindernisse.reset()
                self.schlange.reset()
                 

    def Tod(self): # Schlange trifft sich selbst oder rand, Spiel wird beendet
        global Todesart   
        if not 2 <= self.schlange.body[0].x < Anzahl_Zellen + 2 or not 2 <= self.schlange.body[0].y < Anzahl_Zellen +2 : #Wenn nicht im feld
            Todesart = 1
        
        for Körperteil in self.schlange.body[1:]:
            if Körperteil == self.schlange.body[0] and not self.schlange.body[0] == Vector2(5, 9) and not self.schlange.body[1] == Vector2(4, 9) and not self.schlange.body[2] == Vector2(3,9):
                Todesart = 2
        
        
        if Level == 2 or Level == 3:
            for hindernis in self.hindernisse.Hindernisliste:
                if hindernis == self.schlange.body[0]:
                    Todesart = 3


    def Gras_Feld(self):
    
        GRAS_FARBE = (240,230,140)
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
        frucht_rect = Pilz.get_rect(midright = (score_rect.left, score_rect.centery))

        screen.blit(score_surface, score_rect)
        screen.blit(Pilz, frucht_rect)
        return current_score

    def Highscore(self):
        global safe_score1, Highscore1, safe_score2, Highscore2, Level, Highscore3, safe_score3


        if Level == 1:

            Highscore = Highscore1
            trophy = self.silver_trophy
            if int(safe_score1) > int(Highscore1) and Todesart != 0:
                Highscore1 = safe_score1
                d = shelve.open('score.txt')  
                d['Highscore1'] = Highscore1  
                d.close()
                
        if Level == 2:
            trophy = self.gold_trophy
            Highscore = Highscore2
            if int(safe_score2) > int(Highscore2) and Todesart != 0:
                    Highscore2 = safe_score2
                    d = shelve.open('score.txt')  # here you will save the score variable   
                    d['Highscore2'] = Highscore2           # thats all, now it is saved on disk.
                    d.close()
                    
        if Level == 3:
            trophy = self.rage_trophy
            Highscore = Highscore3
            if int(safe_score3) > int(Highscore3) and Todesart != 0:
                    Highscore3 = safe_score3
                    d = shelve.open('score.txt')
                    d['Highscore3'] = Highscore3          
                    d.close()


        highscore_surface = SCHRIFTART.render(Highscore, True, (56,74,12))
        highscore_x = int(440) #Wo Score Anzeige
        highscore_y = int(40)

        highscore_rect = highscore_surface.get_rect(center = (highscore_x,highscore_y)) #Macht ein rectangle um den Score, und platziert mittif davon
        trophy_rect = self.silver_trophy.get_rect(midright = (highscore_rect.left, highscore_rect.centery))
        screen.blit(highscore_surface, highscore_rect)
        screen.blit(trophy, trophy_rect)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Fonts/font.ttf", size)

def play():
    pygame.display.set_caption("Play")
    global Todesart, es_score, countdown
    Todesart = 0
    countdown = 600
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
        if Level == 3:
            screen.blit(Wüste_BG_4, (0,0))


        Feldrahmen_rect = pygame.Rect(75,75,610,610)        
        pygame.draw.rect(screen, (79, 70, 65), Feldrahmen_rect, 0)
        Feld_rect = pygame.Rect(80,80,600,600)
        pygame.draw.rect(screen, (205,198,115), Feld_rect, 0)

        if Level == 3:
            countdown_text = get_font(40).render(f'{int(countdown/60)}', True, (255, 0, 0))
            countdown_rect = countdown_text.get_rect(center = (690, 40))
            screen.blit(countdown_text,countdown_rect)
            countdown -= 1
            if countdown <= 0:
                play_upside_down()


        main_game.Malen()
        pygame.display.update() #Updatet nach jedem while loop
        clock.tick(FPS) #updatet 60x pro sekunde
        if Todesart != 0:
            spielen = False
            restart()  
            main_game.Highscore()


def play_upside_down(): #Umgedrehte Steuerung
    pygame.display.set_caption("Play")
    global Todesart, es_score, countdown
    Todesart = 0
    countdown = 600
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
                    if main_game.schlange.Richtung.y != -1: #Man kann nur nach oben gehen, wenn man nicht nach unten geht
                        main_game.schlange.Richtung = Vector2(0, 1)

                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if main_game.schlange.Richtung.y != 1:
                        main_game.schlange.Richtung = Vector2(0, -1)

                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if main_game.schlange.Richtung.x != -1:
                        main_game.schlange.Richtung = Vector2(1, 0)
                    
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if main_game.schlange.Richtung.x != 1:
                        main_game.schlange.Richtung = Vector2(-1, 0)
                
        if Level == 1:
            screen.blit(Wüste_BG, (0,0))
        if Level == 2:
            screen.blit(Wüste_BG_2, (0,0))
        if Level == 3:
            screen.blit(Wüste_BG_4, (0,0))


        Feldrahmen_rect = pygame.Rect(75,75,610,610)        
        pygame.draw.rect(screen, (79, 70, 65), Feldrahmen_rect, 0)
        Feld_rect = pygame.Rect(80,80,600,600)
        pygame.draw.rect(screen, (205,198,115), Feld_rect, 0)

        if Level == 3:
            countdown_text = get_font(40).render(f'{int(countdown/60)}', True, (255, 0, 0))
            countdown_rect = countdown_text.get_rect(center = (690, 40))
            screen.blit(countdown_text,countdown_rect)
            countdown -= 1
            if countdown <= 0:
                play()


        main_game.Malen()
        pygame.display.update()
        clock.tick(FPS) 
        if Todesart != 0:
            spielen = False
            restart()  
            main_game.Highscore()

def laden():
    global loading_states, Highscore1, Highscore2, Highscore3, Sterne_lvl_1, Sterne_lvl_2, is_Ton_an
    if loading_states:
            d = shelve.open('score.txt')
            if 'Highscore1' in d:
                Highscore1 = d['Highscore1']
            else: Highscore1 = str(0)
            if 'Highscore2' in d: 
                Highscore2 = d['Highscore2']
            else: Highscore2 = str(0)
            if 'Highscore3' in d:  
                Highscore3 = d['Highscore3']
            else: Highscore3 = str(0)
            if 'Sterne_lvl_1' in d:
                Sterne_lvl_1 = d['Sterne_lvl_1']
            if 'Sterne_lvl_2' in d:  
                Sterne_lvl_2 = d['Sterne_lvl_2']
            if 'is_Ton_an' in d:
                is_Ton_an = d['is_Ton_an']
            d.close()
            loading_states = False

def main_menu():
    pygame.display.set_caption("Main Menu")
    global Todesart
    
    while True:
        if Level == 1:
            screen.blit(Wüste_BG, (0,0))
        if Level == 2:
            screen.blit(Wüste_BG_2, (0,0))
        if Level == 3:
            screen.blit(Wüste_BG_4, (0,0))

        laden()
        Ton_aendern()
        
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
                    main_game.hindernisse.random_hindernisse()
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
    global is_Ton_an
    
    while True:
        d = shelve.open('score.txt') 
        d['is_Ton_an'] = is_Ton_an           
        d.close()

        screen.blit(Wüste_BG_3, (0, 0))
        Ton_aendern()
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
        if is_Ton_an:
            TON_BUTTON = Button(image = pygame.image.load('Sprites/Ton_aus.png'), pos = (700, 715),
                    text_input = '', font = get_font(50), base_color="#d7fcd4", hovering_color = "White")    # Ton kann aus- oder anggeschaltet werden werden
        else:
            TON_BUTTON = Button(image = pygame.image.load('Sprites/Ton_an.png'), pos = (700, 715),
                    text_input = '', font = get_font(50), base_color="#d7fcd4", hovering_color = "White")


        for button in [MAIN_MENU_BUTTON, LEVEL_BUTTON, SKIN_BUTTON, RESET_BUTTON, TON_BUTTON]:
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if TON_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    button_sound.play()
                    if is_Ton_an: is_Ton_an = False
                    else: is_Ton_an = True
                    Ton_aendern()

        pygame.display.update()  

def Ton_aendern():
    global is_Ton_an
    if is_Ton_an:
        button_sound.set_volume(0)
        fail_sound.set_volume(0)
        main_game.schlange.oneup.set_volume(0)
    else:
        button_sound.set_volume(0.4)
        fail_sound.set_volume(0.8)
        main_game.schlange.oneup.set_volume(0.3)

        
def reset_highscore():
    global Highscore1, Highscore2, Highscore3, Sterne_lvl_1, Sterne_lvl_2
    Highscore1 = str(0)
    Highscore2 = str(0)
    Highscore3 = str(0)
    Sterne_lvl_1 = 0
    Sterne_lvl_2 = 0
    d = shelve.open('score.txt')
    d.clear()  
    d.close()


def skins():
    global Farbe
    pygame.display.set_caption("Skins")
    blau_ganze_Schlange =  pygame.image.load('Sprites/blau_ganze_Schlange.png').convert_alpha()
    grun_ganze_Schlange = pygame.image.load('Sprites/grun_ganze_Schlange.png').convert_alpha()
    
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

def unlock_3():
    global Sterne_lvl_1, Sterne_lvl_2, level3_is_unlocked
    if Sterne_lvl_1 == 3 and Sterne_lvl_2 == 3: 
        level3_is_unlocked = True
        return level3_is_unlocked    
    else: 
        level3_is_unlocked = False
        return level3_is_unlocked

def Sternanzeige():
    global Sterne_lvl_1, Sterne_lvl_2
    star_50 = pygame.image.load('Sprites/star_50.png').convert_alpha()
    star_50_grey = pygame.image.load('Sprites/star_50_grey.png').convert_alpha()
    star_80 = pygame.image.load('Sprites/star_80.png').convert_alpha()
    star_80_grey = pygame.image.load('Sprites/star_80_grey.png').convert_alpha()

    #Alle Sterne grau
    Stern1_links_rect = star_50.get_rect(center = (170,215)) #Stern links
    screen.blit(star_50_grey,Stern1_links_rect)
    Stern1_rechts_rect = star_50.get_rect(center = (290,215)) #Stern rechts
    screen.blit(star_50_grey,Stern1_rechts_rect)
    Stern1_mitte_rect = star_80.get_rect(center = (230,200)) #Stern Mitte
    screen.blit(star_80_grey,Stern1_mitte_rect)

    Stern2_links_rect = star_50.get_rect(center = (470,215)) #Stern links
    screen.blit(star_50_grey,Stern2_links_rect)
    Stern2_rechts_rect = star_50.get_rect(center = (590,215)) #Stern rechts
    screen.blit(star_50_grey,Stern2_rechts_rect)
    Stern2_mitte_rect = star_80.get_rect(center = (530,200)) #Stern Mitte
    screen.blit(star_80_grey,Stern2_mitte_rect)

    if Sterne_lvl_1 == 1:
        Stern1_links_rect = star_50.get_rect(center = (170,215))
        screen.blit(star_50,Stern1_links_rect)
    elif Sterne_lvl_1 == 2:
        Stern1_links_rect = star_50.get_rect(center = (170,215))
        screen.blit(star_50,Stern1_links_rect)
        Stern1_rechts_rect = star_50.get_rect(center = (290,215))
        screen.blit(star_50,Stern1_rechts_rect)
    elif Sterne_lvl_1 == 3:
        Stern1_links_rect = star_50.get_rect(center = (170,215))
        screen.blit(star_50,Stern1_links_rect)
        Stern1_rechts_rect = star_50.get_rect(center = (290,215))
        screen.blit(star_50,Stern1_rechts_rect)
        Stern1_mitte_rect = star_80.get_rect(center = (230,200))
        screen.blit(star_80,Stern1_mitte_rect)
    
    if Sterne_lvl_2 == 1:
            Stern2_links_rect = star_50.get_rect(center = (470,215))
            screen.blit(star_50,Stern2_links_rect)
    elif Sterne_lvl_2 == 2:
            Stern2_links_rect = star_50.get_rect(center = (470,215))
            screen.blit(star_50,Stern2_links_rect)
            Stern2_rechts_rect = star_50.get_rect(center = (590,215))
            screen.blit(star_50,Stern2_rechts_rect)
    elif Sterne_lvl_2 == 3:
            Stern2_links_rect = star_50.get_rect(center = (470,215))
            screen.blit(star_50,Stern2_links_rect)
            Stern2_rechts_rect = star_50.get_rect(center = (590,215))
            screen.blit(star_50,Stern2_rechts_rect)
            Stern2_mitte_rect = star_80.get_rect(center = (530,200))
            screen.blit(star_80,Stern2_mitte_rect)

def level():
    global Level, Sterne_lvl_1, Sterne_lvl_2, level3_is_unlocked
    pygame.display.set_caption("Level")
    danger_sign = pygame.image.load('Sprites/danger.png').convert_alpha()
    level_1 = pygame.image.load('Sprites/level_1.PNG').convert_alpha()
    level_2 = pygame.image.load('Sprites/level_2.PNG').convert_alpha()

    while True:  
        screen.blit(Wüste_BG_3, (0, 0))
        LEVEL_MOUSE_POS = pygame.mouse.get_pos()
        LEVEL_TEXT = get_font(50).render("LEVEL WAHL", True, "#b68f40")
        LEVEL_RECT = LEVEL_TEXT.get_rect(center = (380, 75))
        LEVEL_MOUSE_POS = pygame.mouse.get_pos()
        unlock_3()
        Sternanzeige()
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
        
        if Level == 3:
            danger1_rect = danger_sign.get_rect(center = (492, 575))
            danger2_rect = danger_sign.get_rect(center = (268, 575))
            screen.blit(danger_sign, danger1_rect)
            screen.blit(danger_sign, danger2_rect)
     
        LEVEL_BUTTON = Button(image = pygame.image.load("Hintergrund/Restart Rect.png"), pos = (230, 480), 
                            text_input = "Level 1", font = get_font(20), base_color="#d7fcd4", hovering_color = "White")
        LEVEL_BUTTON_2 = Button(image = pygame.image.load("Hintergrund/Restart Rect.png"), pos = (530, 480), 
                            text_input = "Level 2", font = get_font(20), base_color="#d7fcd4", hovering_color = "White")
        if level3_is_unlocked:
            MAIN_MENU_BUTTON = Button(image = pygame.image.load("Hintergrund/Restart Rect.png"), pos = (380, 670), 
                                text_input = "Back", font = get_font(20), base_color="#d7fcd4", hovering_color = "White")
            DANGER_BUTTON = Button(image = pygame.image.load("Hintergrund/Restart Rect.png"), pos = (380, 575), 
                              text_input = "DANGER", font = get_font(20), base_color="#d7fcd4", hovering_color = "Red")
        else:
            MAIN_MENU_BUTTON = Button(image = pygame.image.load("Hintergrund/Restart Rect.png"), pos = (380, 600), 
                                text_input = "Back", font = get_font(20), base_color="#d7fcd4", hovering_color = "White")


        screen.blit(LEVEL_TEXT, LEVEL_RECT)
        if level3_is_unlocked:
            for button in [LEVEL_BUTTON, LEVEL_BUTTON_2, MAIN_MENU_BUTTON, DANGER_BUTTON]:
                button.changeColor(LEVEL_MOUSE_POS)
                button.update(screen) 
        else:
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
            
            if level3_is_unlocked:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if DANGER_BUTTON.checkForInput(LEVEL_MOUSE_POS):
                        button_sound.play()
                        Level = 3
                
        pygame.display.update()     

def restart():
    global es_score, Sterne_lvl_1, Sterne_lvl_2
    fail_sound.play()
    pygame.display.set_caption("Exit Menu")
    meme_suicide = pygame.image.load('Memes\eating ys.jpg').convert_alpha()
    meme_cant_see = pygame.image.load('Memes\cant see.jpg').convert_alpha()
    meme_cactus = pygame.image.load('Memes\cactus.jpg').convert_alpha()
    
    while True:
        if Level == 1: screen.blit(Wüste_BG,(0,0))
        elif Level == 2: screen.blit(Wüste_BG_2,(0,0))
        else: screen.blit(Wüste_BG_4,(0,0))

        DEATH_TEXT = get_font(50).render("You DIED", True, (56,74,12))
        DEATH_RECT = DEATH_TEXT.get_rect(center = (380, 75))
        screen.blit(DEATH_TEXT, DEATH_RECT)

        STAR_TEXT = get_font(20).render(f'You achieved a score of {es_score}', True, (56,74,12))
        STAR_TEXT_RECT = STAR_TEXT.get_rect(center = (380, 120))
        screen.blit(STAR_TEXT, STAR_TEXT_RECT) 
      
        Anzahl_Sterne = int(int(es_score)/10)
        bis_1_stern_Text = get_font(17).render(f'You need {10-int(es_score)} points more for 1 star', True, (56,74,12))
        bis_1_stern_rect = bis_1_stern_Text.get_rect(center = (380, 160))
        bis_2_stern_Text = get_font(17).render(f'You need {20-int(es_score)} points more for 2 stars', True, (56,74,12))
        bis_2_stern_rect = bis_2_stern_Text.get_rect(center = (380, 160))
        bis_3_stern_Text = get_font(17).render(f'You need {30-int(es_score)} points more for 3 stars', True, (56,74,12))
        bis_3_stern_rect = bis_3_stern_Text.get_rect(center = (380, 160))                          
        drei_bekommen_Text = get_font(17).render(f'You got your third Star. Congratulations!', True, (56,74,12))
        drei_bekommen_rect = drei_bekommen_Text.get_rect(center = (380, 160))   

        if Level == 1:
            if Sterne_lvl_1 == 0 and Anzahl_Sterne == 0: screen.blit(bis_1_stern_Text, bis_1_stern_rect)
            elif (Sterne_lvl_1 == 1 and Anzahl_Sterne <= 1): screen.blit(bis_2_stern_Text, bis_2_stern_rect)
            elif Sterne_lvl_1 == 2 and Anzahl_Sterne <= 2: screen.blit(bis_3_stern_Text, bis_3_stern_rect)
            elif Sterne_lvl_1 == 0 and Anzahl_Sterne == 1: Sterne_lvl_1 = 1
            elif Sterne_lvl_1 == 0 and Anzahl_Sterne == 2: Sterne_lvl_1 = 2
            elif Sterne_lvl_1 == 0 and Anzahl_Sterne == 3: Sterne_lvl_1 = 3
            elif Sterne_lvl_1 == 1 and Anzahl_Sterne == 2: Sterne_lvl_1 = 2
            elif Sterne_lvl_1 == 1 and Anzahl_Sterne == 3: Sterne_lvl_1 = 3
            elif Sterne_lvl_1 == 2 and Anzahl_Sterne == 3: Sterne_lvl_1 = 3
            elif Sterne_lvl_1 == 3: screen.blit(drei_bekommen_Text,drei_bekommen_rect)
       
        if Level == 2:
            if Sterne_lvl_2 == 0 and Anzahl_Sterne == 0: screen.blit(bis_1_stern_Text, bis_1_stern_rect)
            elif Sterne_lvl_2 == 1 and Anzahl_Sterne <= 1: screen.blit(bis_2_stern_Text, bis_2_stern_rect)
            elif Sterne_lvl_2 == 2 and Anzahl_Sterne <= 2: screen.blit(bis_3_stern_Text, bis_3_stern_rect)
            elif Sterne_lvl_2 == 3: screen.blit(drei_bekommen_rect,drei_bekommen_rect)
            elif Sterne_lvl_2 == 0 and Anzahl_Sterne == 1: Sterne_lvl_2 = 1
            elif Sterne_lvl_2 == 0 and Anzahl_Sterne == 2: Sterne_lvl_2 = 2
            elif Sterne_lvl_2 == 0 and Anzahl_Sterne == 3: Sterne_lvl_2 = 3
            elif Sterne_lvl_2 == 1 and Anzahl_Sterne == 2: Sterne_lvl_2 = 2
            elif Sterne_lvl_2 == 1 and Anzahl_Sterne == 3: Sterne_lvl_2 = 3
            elif Sterne_lvl_2 == 2 and Anzahl_Sterne == 3: Sterne_lvl_2 = 3
                
        d = shelve.open('score.txt')  #Abspeichern in datei
        d['Sterne_lvl_1'] = Sterne_lvl_1
        d['Sterne_lvl_2'] = Sterne_lvl_2             
        d.close()

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
        
        DEATH_MOUSE_POS = pygame.mouse.get_pos()
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
                    main_game.hindernisse.random_hindernisse()
                    Sterne_lvl_1 = int(es_score)
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
Highscore3 = str(0)
safe_score1 = str(0)
safe_score2 = str(0)
safe_score3 = str(0)

#Laden von ressourcen
SCHRIFTART = pygame.font.Font('Fonts/font.ttf', 25)

Pilz = pygame.image.load('Sprites\Pilz.png').convert_alpha() #convert: ändert Bild in besseres Format für python
fail_sound = pygame.mixer.Sound('Sounds\Fail.mp3')
fail_sound.set_volume(0.8)
button_sound = pygame.mixer.Sound('Sounds/button.mp3')
button_sound.set_volume(0.4)
haekchen = pygame.image.load('Sprites/häkchen.PNG').convert_alpha()
Wüste_BG = pygame.image.load('Hintergrund/desert.jpg').convert_alpha()
Wüste_BG_2 = pygame.image.load('Hintergrund/desert2.jpg').convert_alpha()
Wüste_BG_3 = pygame.image.load('Hintergrund/desert3.png').convert_alpha()
Wüste_BG_4 = pygame.image.load('Hintergrund/desert4.jpg').convert_alpha()
Cactus_1 = pygame.image.load('Sprites/cactus_1.png').convert_alpha()
Cactus_2 = pygame.image.load('Sprites/cactus_2.png').convert_alpha()
Cactus_3 = pygame.image.load('Sprites/cactus_3.png').convert_alpha()
Cactus_4 = pygame.image.load('Sprites/cactus_4.png').convert_alpha()

#Startoptions
Farbe = 'Blau'
Level = 1 
Sterne_lvl_1 = 0
Sterne_lvl_2 = 0
es_score = 0
level3_is_unlocked = False
is_Ton_an = True

countdown = 600
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
