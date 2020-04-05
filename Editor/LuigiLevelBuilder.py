import os, pygame
from pygame.locals import *
from LuigiLEHandlers import *
from LevelClass import *

# File to modify
filename = 'world1-1.txt'
# Change these to change the screen size
BLOCKSCALEFACTOR = 2
HORIZTILES = 25
VERTTILES = 15

# Derived values, don't change these
# Global Variable Declarations
mainLoopRunning = True
clock = pygame.time.Clock()
# Screen settings
BLOCKRESO = 16
screenWidth = HORIZTILES * BLOCKRESO * BLOCKSCALEFACTOR
screenHeight = VERTTILES * BLOCKRESO * BLOCKSCALEFACTOR
screen = pygame.display.set_mode((screenWidth, screenHeight))
screenInfo = (BLOCKSCALEFACTOR, HORIZTILES, VERTTILES, BLOCKRESO)
# Create the background
background = pygame.Surface(screen.get_size())
background.fill((99, 155, 255))
background = background.convert()
# Set up the window
pygame.init()
pygame.display.set_caption("Luigi Level Editor")
pygame.mouse.set_visible(1)

myLevel = Level(filename, screenInfo)

# Set up the textures for blitting
# This list is how we'll reference the textures, and so the order matters
textureNames = ['SelectBox', 'Bricks', 'Cloud1', 'Cloud2', 'Cloud3', 'Coin1', 'Mushroom',
                'Flagpole', 'FlagTop', 'Floortile', 'Goomba', 'GroundBlock',
                'Luigi', 'TubeBody', 'TubeTop', 'Turtle']
textures = {}
for name in textureNames:
    imgSurf = pygame.image.load(os.path.join('../Sprites', name + '.png'))
    scaledReso = BLOCKRESO * BLOCKSCALEFACTOR
    imgSurf = pygame.transform.scale(imgSurf, (scaledReso, scaledReso))
    imgSurf = imgSurf.convert_alpha()
    textures[name] = imgSurf

# Vars to control the player selection and viewport
select_x = 0
select_y = 0
camera_x = 0
camera_y = 0
selected = 0

saveLevel = False

while mainLoopRunning:
    # Don't need a tick handler
    clock.tick(30)

    # Look at the queue for the exit event
    for event in pygame.event.get():
        if event.type == QUIT:
            mainLoopRunning = False
        keystate = pygame.key.get_pressed()
        if keystate[K_LEFT]:
            select_x = min(HORIZTILES - 1, max(0, select_x - 1))
        if keystate[K_RIGHT]:
            select_x = min(HORIZTILES - 1, max(0, select_x + 1))
        if keystate[K_DOWN]:
            select_y = min(VERTTILES - 1, max(0, select_y + 1))
        if keystate[K_UP]:
            select_y = min(VERTTILES - 1, max(0, select_y - 1))
        if keystate[K_SPACE]:
            myLevel.stamp(selected, select_x, select_y, camera_x, camera_y)
        if keystate[K_BACKSPACE]:
            myLevel.stamp(0, select_x, select_y, camera_x, camera_y)
        if keystate[K_q]:
            selected = (selected - 1) % len(textureNames)
        if keystate[K_e]:
            selected = (selected + 1) % len(textureNames)
        if keystate[K_a]:
            camera_x = max(0, (camera_x - 1))
        if keystate[K_d]:
            camera_x = camera_x + 1
            myLevel.validateRight(camera_x, screenInfo)
        if keystate[K_l]:
            saveLevel = True
            mainLoopRunning = False

    # Draw the Screen
    drawScreen(screen, background, myLevel.getSlice(camera_x, camera_y, screenInfo), textureNames, textures,
               (select_x, select_y), selected, screenInfo)
    pygame.display.flip()

if saveLevel:
    print("Saving level...")
    myLevel.save()
pygame.quit()
