import pygame, sys
import story
from pygame.locals import *

WHITE = (255, 255, 255)
ORANGE = (214, 66, 255) 
BLACK = (0,0,0)


# Routine taken from:  https://www.pygame.org/wiki/TextWrap
#
# draw some text into an area of a surface
# automatically wraps words
# returns any text that didn't get blitted
def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    rect = Rect(rect)
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text


def draw_background(surface, scene):
    """ Draw the main screen background """

    surface.fill(WHITE)

    pygame.draw.line(surface, BLACK, (0, 50), (1024, 50), 5)
    pygame.draw.line(surface, BLACK, (600, 50), (600, 768), 5)
    pygame.draw.line(surface, BLACK, (0, 625), (600, 625), 5)

    title_font = pygame.font.SysFont('Arial', 30)
    title_surface = title_font.render('Mooky Skiing Mystery', True, (0, 0, 0))
    surface.blit(title_surface, (350, 10))

    image = pygame.image.load(scene[1])
    image = pygame.transform.scale(image, (400, 400))
    surface.blit(image, (605, 53))

def draw_options(surface, scene):
   
    options = scene[2]
    
    row = 635
    for (optiontext, optionkey) in options: 
        text_font = pygame.font.SysFont('Arial', 20)
        text_surface = text_font.render(optiontext, True, (0, 0, 0))
        surface.blit(text_surface, (10, row))
        row += 25 


def draw_text(surface, scene):

    maintext_font = pygame.font.SysFont('Arial', 20)
    maintext_surface = maintext_font.render(scene[0], True, (0, 0, 0))
    surface.blit(maintext_surface, (10, 200))


def main():
    pygame.init()
    pygame.font.init()
    surface = pygame.display.set_mode((1024, 768), 0, 32)

    FPS = 30 # frames per second setting
    fpsClock = pygame.time.Clock()

    scene = story.get_first_scene()

    # set up the window
    pygame.display.set_caption("Mooky's Ski Mystery")

    keystate = None

    while True: # the main game loop
        draw_background(surface, scene)
        draw_options(surface, scene)
        draw_text(surface, scene)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keystate = pygame.key.get_pressed()

        pygame.display.update()
        fpsClock.tick(FPS)


if __name__ == "__main__":
    main()

