import math
from datetime import datetime

def getLengthBettweenPoints(x1, y1, x2, y2):
    return math.sqrt(pow(abs(x1 - x2), 2) + pow(abs(y1 - y2), 2))

def getTimesDiffrence(time):
    return (datetime.now() - time).total_seconds()

def getSpeedOfPoints(x1, y1, x2, y2, time):
    lbp = getLengthBettweenPoints(x1, y1, x2, y2)
    speed = lbp / time

    return speed

def getBoostOfSpeed(speed, time):
    return speed / time;