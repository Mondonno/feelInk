import pygame

from constants import *
from utils import *

from datetime import datetime
from math import sqrt

lastTime = datetime.now()
lastSpeed = None

currentX = None
currentY = None

penOn = False
mouseStatus = True
brushSize = STANDARD_BRUSH_SIZE

def handleMotion(screen):
    global currentX
    global currentY
    global lastTime
    global penOn
    global lastSpeed

    (mX, mY) = pygame.mouse.get_pos()

    if currentX == None or currentY == None:
        currentX = mX
        currentY = mY
            
    speed = getSpeedOfPoints(currentX, currentY, mX, mY, lastTime)

    if lastSpeed != None:
        abbs = abs(lastSpeed - speed)

    if (lastSpeed != None
        and abbs <= TOUCH_PAD_MACOS_CONSISTENCY
        and mouseStatus == False):
        penOn = True
    elif penOn == True:
        penOn = False

    if penOn == True:
        if BRUSH_TYPE == 0:
            pygame.draw.circle(screen, (0,0,0), (mX, mY), brushSize)
        else:
            pygame.draw.line(screen, (0,0,0), (currentX, currentY), (mX, mY), width=brushSize)

    lastTime = datetime.now()
    lastSpeed = speed

    currentX = mX
    currentY = mY

def saveBoard(screen):
    saveToPath = createOutputFilePath(SAVE_FILE_PATH, SAVE_FILE_NAME, SAVE_FILE_EXT)

    try:
        pygame.image.save(screen, saveToPath)
    except pygame.error:
        print(pygame.get_error())

def main():
    pygame.init()

    global mouseStatus

    icon = pygame.transform.scale(loadImage(ICON_PATH), (32, 32))
    pygame.display.set_icon(icon)
    pygame.display.set_caption(TITLE)

    screen = pygame.display.set_mode([BOARD_X_DISSMENSION, BOARD_Y_DISSMENSION],1)
    screen.fill((255, 255, 255))

    clock = pygame.time.Clock()

    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                return

            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_s:
                    saveBoard(screen)

            if events.type == pygame.MOUSEBUTTONDOWN:
                if mouseStatus == True:
                    mouseStatus = False
                else: mouseStatus = True

            if events.type == pygame.MOUSEMOTION:
                handleMotion(screen)

        pygame.display.flip()
        clock.tick(40)

    pygame.quit()

try:
    main()
except KeyboardInterrupt:
    print("\n KeyboardInterreput: Exiting....")
