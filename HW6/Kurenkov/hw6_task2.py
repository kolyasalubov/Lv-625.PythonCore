# Write a program that calculates the square of a rectangle, triangle and circle
# (write three functions to calculate the square, and call them in the main program depending on the user's choice).
from math import pi, sqrt


def rectangle_square(p, d):
    return round((p * d), 3)


def triangle_square(a, b, c):
    sp = (a + b + c) / 2
    return round(sqrt(sp*(sp-a)*(sp-b)*(sp-c)), 3)


def circle_square(r):
    return round(pi * r ** 2, 3)


def simple_square(*args):
    """ This function can define a square of a rectangle, triangle, or circle, using only the length of their sides
    or radius accordingly.
    All that you need is to pass to the function two parameters for the rectangle, three for the triangle, or one
    for the circle and fetch the results.
    """

    if len(args) == 2:
        print(rectangle_square(*args))
    elif len(args) == 1:
        print(circle_square(*args))
    elif len(args) == 3:
        print(triangle_square(*args))
    else:
        print("This is a simple function, so it can use only specific parameters, please use help for more info.")



