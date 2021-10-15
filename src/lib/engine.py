from .data import *
from .events import *
from misc.constants import *

class MiceInk():
    def __init__(self, screen, parent):
        self.data = MiceInkData()

        self.screen = screen
        self.parent = parent

        self.events = {}
        self.eventsHandler = MiceInkEvents(self)

        self.loadEvents()

    def createNewBoard(self):
        self.screen.fill(BOARD_COLOR)

    def loadEvents(self):
        self.events = self.eventsHandler.getEvents()

    def executeEvent(self, event):
        eventName = pygame.event.event_name(event.type)
        if not eventName in self.events:
            return None

        foundEvents = self.events[eventName]
        for ev in foundEvents:
            ev(self.eventsHandler,self.screen, event)

    def handleLoop(self, eventsData):
        self.handleEvents(eventsData)

    def handleEvents(self, eventsList):
        for event in eventsList:
            self.executeEvent(event)
