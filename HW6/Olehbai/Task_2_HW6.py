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

figure = input("Choose want do you want to do\n"
            "1 - rectangle\n"
            "2 - triangle\n"
            "3 - circle\n")

if figure == "1":
    print(rectangle())
elif figure == "2":
    print(triangle())
elif figure == "3":
    print(circle())    