import area_of_figures as my_area

figure = int(input("Whot of the figures are you wont to calculate to square? 1 - rectangle 2 - triangle 3 - circle? "))
if figure == 1:
    side1 = int(input("enter the length of the first side "))
    side2 = int(input("enter the length of the second side "))
    print(f"square of a rectangle = {my_area.area_rectangle(side1, side2)}")
elif figure == 2:
    base = int(input("enter the length of the base "))
    height = int(input("enter the length of the height "))
    print(f"square of a triangle = {my_area.area_triangle(base, height):.2f}")
else:
    radius = int(input("enter the length of the radius "))
    print(f"square of a circle = {my_area.area_circle(radius):.2f}")