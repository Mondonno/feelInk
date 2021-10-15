import pygame

from misc.utils import *
from misc.constants import *

from .engine import *

class MiceInkStartup():
    def __init__(self):
        self.clock = pygame.time.Clock()
        
        self.screen = None
        self.engine = None

        self.running = False

    def getPygame(self):
        return pygame

    def getIcon(self):
        return pygame.transform.scale(loadImage(ICON_PATH), (32, 32))

    def initPygame(self):
        pygame.init()

    def initDisplay(self):
        pygame.display.set_icon(self.getIcon())
        pygame.display.set_caption(TITLE)

        self.screen = pygame.display.set_mode([BOARD_X_DISSMENSION, BOARD_Y_DISSMENSION],1)

    def initEngine(self):
        self.engine = MiceInk(self.screen, self)

    def initLoop(self):
        self.running = True

        while self.running:
            self.engine.handleLoop(pygame.event.get())

            self.clock.tick(FRAME_TICK)
            pygame.display.flip()
    
    def initMisc(self):
        self.engine.createNewBoard()
    
    def start(self):
        self.initPygame()
        self.initDisplay()
        self.initEngine()
        self.initMisc()
        self.initLoop()
