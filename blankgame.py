import pygame,sys
from pygame.locals import *
pygame.init()# initialises the pygame
DISPLAYSURF = pygame.display.set_mode((400,300)) # setting up display size
pygame.display.set_caption('~~~~~Pragati Kumar Singh~~~~~') # Setting the Caption
while True:
    for sth in pygame.event.get(): # some sort of event handling function
        if sth.type == QUIT: # It checks if we pressed the QUIT(X) button
            pygame.quit()    # exits pygame
            sys.exit()       # exits python , and hence code stops
    pygame.display.update()  # updates the changes(if any,after one loop) to the screen
