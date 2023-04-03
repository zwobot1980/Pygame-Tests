import pygame

pygame.init()

# Fenstergröße
win_width = 800
win_height = 600

# Hintergrundbild laden
bg = pygame.image.load("weltall_01.png").convert()

# Hintergrundbild positionieren
bg_x = 0
bg_y = 0

# Fenster erstellen
win = pygame.display.set_mode((win_width, win_height))

# Uhr für FPS-Regelung erstellen
clock = pygame.time.Clock()

# Hauptspiel-Schleife
while True:
    # FPS-Regelung
    clock.tick(60)

    # Ereignisschleife
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Hintergrundbild bewegen
    bg_y += 5

    # Wenn das Bild vollständig aus dem Fenster gescrollt ist, setze die Position zurück
    if bg_y > bg.get_height():
        bg_y = 0

    # Hintergrundbild anzeigen
    win.blit(bg, (bg_x, bg_y - bg.get_height()))
    win.blit(bg, (bg_x, bg_y))

    # Fenster aktualisieren
    pygame.display.update()
