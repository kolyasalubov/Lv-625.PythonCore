import math
def distance(x1, y1, x2, y2):
    return round(float(math.sqrt(abs(x2 - x1)**2 + abs(y2 - y1)**2)), 2)
