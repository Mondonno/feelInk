from datetime import datetime
from misc.constants import STANDARD_BRUSH_SIZE

class MiceInkData():
    def __init__(self):
        self.lastTime = datetime.now()
        self.lastSpeed = None

        self.currentX = None
        self.currentY = None

        self.penOn = False
        self.mouseStatus = True

        self.brushSize = STANDARD_BRUSH_SIZE
