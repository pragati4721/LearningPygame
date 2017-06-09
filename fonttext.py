import pygame,sys
from pygame.locals import *
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption("~~~Texttraining@Pragati~~~")
WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE =(0,0,255)
fontObj = pygame.font.Font('freesansbold.ttf',32)
textSurfaceObj = fontObj.render('Hello ~~~~~Pragati~~~~~',True,GREEN,BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200,150)
while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj,textRectObj)
    for sth in pygame.event.get():
        if sth.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
