import math
def rectangle(a, b):
    # Function will calculate the squere of the rectangle
    s_r = a*b
    return round((s_r), 2)
def triangle(a, b, c):
    # Function will calculate the squere of the triangle
    p = (a+b+c)/2
    s_t = round(math.sqrt(p*(p-a)*(p-b)*(p-c)), 2)
    return s_t
def circle(r):
    # The function will calculate the squere of the circle
    s_c = math.pi*(r**2)
    return round((s_c), 2)

figure = int(input("Select the figure for squere calculation: 1. Rectangle, 2. Triangle, 3. Circle "))
if figure == 1:
    side_rect_a = float(input("Input side a: "))
    side_rect_b = float(input("Input side b: "))
    print(f"The squere of rectangle is: {rectangle(side_rect_a, side_rect_b)}")
elif figure == 2:
    side_trian_a = float(input("Input side a: "))
    side_trian_b = float(input("Input side b: "))
    side_trian_c = float(input("Input side c: "))
    print(f"The squere of the triangle is: {triangle(side_trian_a, side_trian_b, side_trian_c)}")
elif figure == 3:
    rad_cir = float(input("Input circle radius: "))
    print(f"The squere of the circle is: {circle(rad_cir)}")
