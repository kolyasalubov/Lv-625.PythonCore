##### https://www.codewars.com/kata/simple-find-the-distance-between-two-points
"""
Given two ordered pairs calculate the distance between them. 
Round to two decimal places. This should be easy to do in 0(1) timing.
"""

def distance(x1, y1, x2, y2):
    """
    Finding the distance between two points.
    The distance between two points is the length of the line 
    joining the two points in the coordinate plane.
    To find the distance between two points in the coordinate plane, 
    we make use of the formula d = sqrt((x2 - x1)^2 + (y2 - y1)^2).
    Сoordinates of the first point: (x1, y1)
    Сoordinates of the second point: (x2, y2)
    """
    D = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
    return round(D,2)

print(distance(-3, 4, 2, -4))   # 9.43

