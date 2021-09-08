import Modul_for_calc_figures as calc_fig


figure = int(input("Whot of the figures are you wont to calculate to square? 1 - rectangle 2 - triangle 3 - circle? "))
if figure == 1:
    side1 = int(input("enter the length of the first side "))
    side2 = int(input("enter the length of the second side "))
    print(f"square of a rectangle = {calc_fig.square_rectangle(side1, side2)}")
elif figure == 2:
    our_tupl = ('first','second','third')
    our_sides = [(int(input(f"enter the length of the {i} side "))) for i in our_tupl]
    # our_sides = []
    # our_tupl = ('first','second','third')
    # for i in our_tupl:
    #     our_sides.append(int(input(f"enter the length of the {i} side ")))

    # # side1 = int(input("enter the length of the first side "))
    # # side2 = int(input("enter the length of the second side "))
    # # side3 = int(input("enter the length of the third side "))
    # # print(f"square of a triangle = {calc_fig.square_triangle(side1, side2, side3):.2f}")
    print(f"square of a triangle = {calc_fig.square_triangle(our_sides):.2f}")
else:
    radius = int(input("enter the length of the radius "))
    print(f"square of a circle = {calc_fig.square_circle(radius):.2f}")
