import pygame

from constants import *
from utils import *

from datetime import datetime
from math import sqrt

pygame.init()

pygame.display.set_icon(pygame.transform.scale(loadImage(ICON_PATH), (32, 32)))
pygame.display.set_caption(TITLE)

lastTime = datetime.now()

currentX = None
currentY = None

penOn = False
mouseStatus = False
brushSize = 3

screen = pygame.display.set_mode([700, 700],0)
screen.fill((255, 255, 255))

clock = pygame.time.Clock()

# screen = pygame.display.set_mode((640, 480), 0)

while True:
    for events in pygame.event.get():
        if events.type == pygame.MOUSEBUTTONDOWN:
            if mouseStatus == True:
                mouseStatus = False
            else: mouseStatus = True

        if events.type == pygame.MOUSEMOTION:
            (mX, mY) = pygame.mouse.get_pos()

            if currentX == None or currentY == None:
                currentX = mX
                currentY = mY
            
            lbp = getLengthBettweenPoints(currentX, currentY, mX, mY)
            time = (datetime.now() - lastTime).total_seconds()
            speed = lbp / time

            if speed <= TOUCH_PAD_MACOS_SPEED and mouseStatus == False:
                penOn = True
            elif penOn == True:
                penOn = False

            if penOn == True:
                pygame.draw.circle(screen, (0,0,0), (mX, mY), brushSize)
                # pygame.draw.line(screen, (0,0,0), (currentX, currentY), (mX, mY), width=10)

            lastTime = datetime.now()

            currentX = mX
            currentY = mY

    pygame.display.flip()
    clock.tick(40)

pygame.quit()