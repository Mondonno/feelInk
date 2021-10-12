import os
import math
import pygame

def loadImage(file):
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface

def getLengthBettweenPoints(x1, y1, x2, y2):
    return math.sqrt(pow(abs(x1 - x2), 2) + pow(abs(y1 - y2), 2))
