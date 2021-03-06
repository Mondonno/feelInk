from datetime import datetime
from misc.constants import STANDARD_BRUSH_SIZE

class InkData():
    def __init__(self):
        self.lastTime = datetime.now()
        self.lastBoost = None

        self.currentX = None
        self.currentY = None

        self.penOn = False
        self.mouseStatus = True

        self.brushSize = STANDARD_BRUSH_SIZE
