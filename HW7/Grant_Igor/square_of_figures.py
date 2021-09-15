import math
def triangle():
    # Function will calculate the square of the triangle
    basis = float(input("Input basis: "))
    height = float(input("Input height: "))
    return ("The square of the triangle is: {}".format(round((0.5 * basis * height), 2)))

def rectangle():
    # Function will calculate the square of the rectangle
    width = float(input("Input width: "))
    height = float(input("Input height: "))
    return ("The square of rectangle is: {}".format(round((width * height), 2)))

def circle():
    # Function will calculate the square of the circle
    radius = float(input("Input radius: "))
    return ("The square of the circle is: {}".format(round((math.pi*pow(radius, 2)), 2)))
