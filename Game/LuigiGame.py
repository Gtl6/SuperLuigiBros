import os, pygame
from pygame.locals import *
from LuigiGameHandlers import *
from Level import Level
from Screen import Screen
from Controller import Controller, KeyboardButton

# File to modify
filename = 'world1-1.txt'

# Set up the window
pygame.init()
pygame.display.set_caption("Luigi Game (2020)")
pygame.mouse.set_visible(1)

# Set up input
myController = Controller()
myController.register_button('up', KeyboardButton(pygame.K_UP))
myController.register_button('down', KeyboardButton(pygame.K_DOWN))
myController.register_button('left', KeyboardButton(pygame.K_LEFT))
myController.register_button('right', KeyboardButton(pygame.K_RIGHT))
myController.register_button('jump', KeyboardButton(pygame.K_a))
myController.register_button('action', KeyboardButton(pygame.K_f))

# Handling time
clock = pygame.time.Clock()

# Set up the screen
BLOCKSCALEFACTOR = 2
HORIZTILES = 25
VERTTILES = 15
BLOCKRESO = 16
screenWidth = HORIZTILES * BLOCKRESO * BLOCKSCALEFACTOR
screenHeight = VERTTILES * BLOCKRESO * BLOCKSCALEFACTOR
myScreen = Screen(screenWidth, screenHeight)
# Also set up out default background for the game
myBackground = pygame.Surface((screenWidth, screenHeight))
myBackground.fill((99, 155, 255))
myBackground = myBackground.convert()
myScreen.set_background(myBackground)

running = True
while running:
    # Capping the game at 30 FPS
    timeDelta = clock.tick(30)

    # Look at the queue for the exit event
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    myScreen.draw()


pygame.quit()
