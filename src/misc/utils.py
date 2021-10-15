import os
import math
import pygame
from datetime import datetime

## IMAGE & FILES UTILS ##

def loadImage(file):
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    
    return surface

# creates output file path with current date (to be unique)
def createOutputFilePath(path, name, ext):
    nowStr = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    newStrName = name + " " + nowStr
    newLegName = newStrName + "." + ext

    newPath = os.path.join(path, newLegName)
    return newPath

## MATH UTILS ##

def getLengthBettweenPoints(x1, y1, x2, y2):
    return math.sqrt(pow(abs(x1 - x2), 2) + pow(abs(y1 - y2), 2))

def getSpeedOfPoints(x1, y1, x2, y2, lastTime):
    lbp = getLengthBettweenPoints(x1, y1, x2, y2)
    time = (datetime.now() - lastTime).total_seconds()
    speed = lbp / time

    return speed