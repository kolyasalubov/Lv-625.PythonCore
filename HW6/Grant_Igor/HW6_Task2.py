from sqr_rectangle import rectangle as s_r
from sqr_triangle import triangle as s_t
from sqr_circle import circle as s_c
figure = int(input("Select the figure for squere calculation: 1. Rectangle, 2. Triangle, 3. Circle "))
if figure == 1:
    side_rect_a = float(input("Input side a: "))
    side_rect_b = float(input("Input side b: "))
    print(f"The squere of rectangle is: {s_r(side_rect_a, side_rect_b)}")
elif figure == 2:
    side_trian_a = float(input("Input side a: "))
    side_trian_b = float(input("Input side b: "))
    side_trian_c = float(input("Input side c: "))
    print(f"The squere of the triangle is: {s_t(side_trian_a, side_trian_b, side_trian_c)}")
elif figure == 3:
    rad_cir = float(input("Input circle radius: "))
    print(f"The squere of the circle is: {s_c(rad_cir)}")
