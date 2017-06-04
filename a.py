import pygame# importing the library
import time
import random
pygame.init()#initialising the pygame
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))#setting display size to 800*600
pygame.display.set_caption('Slither')#setting title
img = pygame.image.load('snake.png')
clock = pygame.time.Clock()
block_size = 30
fps = 30
direction = "right"
font = pygame.font.SysFont(None,25)
def snake(block_size,snakeList):
    if direction == "right":
        head = pygame.transform.rotate(img,270)
    if direction == "left":
        head = pygame.transform.rotate(img,90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img,180)
    gameDisplay.blit(head,(snakeList[-1][0],snakeList[-1][1]))
    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay,green,[XnY[0],XnY[1],block_size,block_size])
def text_objects(text,color):
    textSurface = font.render(text,True,color)
    return textSurface,textSurface.get_rect()
def message_to_screen(msg,color):
    textSurf,textRect = text_objects(msg,color)
    #screen_text = font.render(msg,True,color)
    #gameDisplay.blit(screen_text,[display_width/2,display_height/2])
    textRect.center = (display_width/2),(display_height/2)
    gameDisplay.blit(textSurf,textRect)
def gameLoop():
    global direction
    gameExit = False
    gameOver = False
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 10
    lead_y_change = 0
    snakeList = []
    snakeLength = 1
    randAppleX = round(random.randrange(0,display_width-block_size))#/10.0)*10.0
    randAppleY = round(random.randrange(0,display_height - block_size))#/10.0)*10.0
    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit",red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:

                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            #print event
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0
        if lead_x>=display_width or lead_x<0 or lead_y >=display_height or lead_y<0:
            gameOver = True
            #if event.type == pygame.KEYUP:
            #    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            #       lead_x_change = 0
        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(white)
        appleThickness = 30
        pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,appleThickness,appleThickness])

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        if len(snakeList)>snakeLength:
            del snakeList[0]
        for eachSegment in snakeList[:-1]:
            if eachSegment== snakeHead:
                gameOver = True
        snake(block_size,snakeList)
        #pygame.draw.rect(gameDisplay,red,[400,300,10,10])
        #gameDisplay.fill(red,rect = [200,200,50,50])
        pygame.display.update()
        # if lead_x >= randAppleX and lead_x <= randAppleX+appleThickness:
        #     if lead_y >= randAppleY and lead_y <= randAppleY+appleThickness:
        #
        if lead_x > randAppleX and lead_x < randAppleX + appleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + appleThickness:
            #print "xcrpp"
            if lead_y > randAppleY and lead_y < randAppleY +appleThickness:
                randAppleX = round(random.randrange(0,display_width-block_size))#/10.0)*10.0
                randAppleY = round(random.randrange(0,display_height - block_size))#/10.0)*10.0
                snakeLength+=1
            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + appleThickness:
                randAppleX = round(random.randrange(0,display_width-block_size))#/10.0)*10.0
                randAppleY = round(random.randrange(0,display_height - block_size))#/10.0)*10.0
                snakeLength+=1
        clock.tick(fps)
    pygame.quit()#quitting the pygame
    quit()#quitting terminal
gameLoop()
