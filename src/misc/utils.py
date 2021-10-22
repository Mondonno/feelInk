import os
import math
import pygame
from datetime import datetime

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