def square_rectangle(n1 : int, n2 : int):
    """
    calculates the square of ​​a rectangle
    """
    return(int(n1 * n2))
def square_triangle(n1 : int, n2 : int, n3 : int):
    """
    calculates the square of ​​a triangle
    """
    p = (n1 + n2 + n3)/2
    return(float(p * (p - n1) * (p - n2) * (p - n3)) ** 0.5)
def square_circle(radius : int):
    """
    calculates the square of ​​a circle 
    """
    return(3.14 * radius ** 2)

figure = int(input("Whot of the figures are you wont to calculate to square? 1 - rectangle 2 - triangle 3 - circle? "))
if figure == 1:
    side1 = int(input("enter the length of the first side "))
    side2 = int(input("enter the length of the second side "))
    print(f"square of a rectangle = {square_rectangle(side1, side2)}")
elif figure == 2:
    side1 = int(input("enter the length of the first side "))
    side2 = int(input("enter the length of the second side "))
    side3 = int(input("enter the length of the third side "))
    print(f"square of a triangle = {square_triangle(side1, side2, side3):.2f}")
else:
    radius = int(input("enter the length of the first side "))
    print(f"square of a circle = {square_circle(radius):.2f}")
