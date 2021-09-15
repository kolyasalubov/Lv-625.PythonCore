
from math import pi
def rectangle(lenght, width):
    return (f"The square of rectangle is {lenght*width}")
def triangle(lenght, height):
    return(f"The square of triangle is {0.5 * lenght*height}")
def circle(radius):
    return (f"The square of circle is {pi * radius**2}")
square = True
while square:
    choose_figure= input("Enter name of this figure: rectangle, triangle or circle what you need to calculate the square ")
    if choose_figure == "rectangle":
        print("Please enter the parametrs of figure")
        lenght = int(input("Enter lenght of rectangle: "))
        width = int(input("Enter widht of rectangle: "))
        square_rectangle = rectangle(lenght, width)
        print(square_rectangle)
        break
    elif choose_figure == "triangle":
        print("Please enter the parametrs of figure")
        lenght=int(input("Enter lenght of triangle: "))
        height = int(input("Enter heigt of triangle: "))
        square_of_triangle=triangle(lenght, height)
        print(square_of_triangle)
        break
    elif choose_figure == "circle":
        print("Please enter the parametrs of figure")
        radius = int(input("Enter radius of circle: "))
        square_of_cirle =  circle(radius)
        print(square_of_cirle)
        break
    else:
        print("Something wrong, try another figure")

