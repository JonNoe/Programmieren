import pygame

BREITE, HOEHE = 900, 500
WINDOW = pygame.display.set_mode((BREITE,HOEHE))
WHITE = (255, 255, 255)
FPS = 30

pygame.display.set_caption("Spiel toll")

#Import Images
SKELETT = 

def draw_window():
        WINDOW.fill(WHITE) #Window mit WHITE füllen
        pygame.display.update()


def main ():
    clock = pygame.time.clock()
    run = True #SOrgt dafür, dass das Spiel offen bleibt
    while run:
        clock.tick(FPS)
        for event in pygame.event.get(): #for Loop für das Beenden des Fensters
            if event.type == pygame.QUIT:
                run = False
        
        draw_window() #Funktion für den Hintergrund

    
    pygame.quit()

#Startet nur das Spiel, wenn diese Datei direkt geöffnet wird
if __name__ == "__main__": #__name__ ist der Name des files und __main__ ist das main file
    main()
            