import pygame, sys
from pygame.locals import *

WHITE = (255, 255, 255)
ORANGE = (214, 66, 255) 
BLACK = (0,0,0)

DISPLAYSURF = pygame.display.set_mode((1024, 768), 0, 32)

def draw_background():
    """ Draw the main screen background """

    DISPLAYSURF.fill(WHITE)

    pygame.draw.line(DISPLAYSURF, BLACK, (0, 50), (1024, 50), 5)
    pygame.draw.line(DISPLAYSURF, BLACK, (600, 50), (600, 768), 5)
    pygame.draw.line(DISPLAYSURF, BLACK, (0, 625), (600, 625), 5)

    title_font = pygame.font.SysFont('Arial', 30)
    title_surface = title_font.render('Mooky Skiing Mystery', False, (0, 0, 0))
    DISPLAYSURF.blit(title_surface, (350, 10))

    mooky_image = pygame.image.load('mooky.png')
    mooky_image = pygame.transform.scale(mooky_image, (400, 400))
    DISPLAYSURF.blit(mooky_image, (605, 53))

def draw_options():

    text_font = pygame.font.SysFont('Arial', 20)
    text_surface = text_font.render('a.', False, (0, 0, 0))
    DISPLAYSURF.blit(text_surface, (10, 635))


def main():
    pygame.init()
    pygame.font.init()

    FPS = 30 # frames per second setting
    fpsClock = pygame.time.Clock()

    # set up the window
    pygame.display.set_caption("Mooky's Ski Mystery")

    keystate = None

    while True: # the main game loop
        draw_background()
        draw_options()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keystate = pygame.key.get_pressed()

        pygame.display.update()
        fpsClock.tick(FPS)


if __name__ == "__main__":
    main()

