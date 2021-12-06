from math import pi
from math import pow

def triangle_square():
    base=int(input("please enter triangle base: "))
    height=int(input("please enter triangle height: "))
    sq_tri=1/2*(base*height)
    return sq_tri

def rectangle_square():
    width=int(input("please enter rectangle width: "))
    height=int(input("please enter rectangle height: "))
    sq_rect=(width*height)
    return sq_rect

def circle_square():
    radius=int(input("please enter circle radius: "))
    # PI=3.141592653589793
    sq_circle=pi*pow(radius,2)
    return sq_circle.__round__(2)