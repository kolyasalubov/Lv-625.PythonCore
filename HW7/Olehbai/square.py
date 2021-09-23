from math import pi
def rectangle():
    side_1 = float(input("Enter side 1: "))
    side_2 = float(input("Enter side 2: "))
    return f"Square of rectangle is = {side_1 * side_2}"

def triangle():
    a = float(input("Enter a: "))
    h = float(input("Enter h: "))
    return f"Square of triangle is = {a * h * 0.5}"
def circle():
    r = float(input("Enter r: "))
    return f"Square of circle is = {pi * (r**2)}"
    