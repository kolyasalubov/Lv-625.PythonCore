import square as sq
figure = int(input("Select the figure for square calculation: 1. Rectangle, 2. Triangle, 3. Circle "))
if figure == 1:
    side_rect_a = float(input("Input side a: "))
    side_rect_b = float(input("Input side b: "))
    print(f"The square of rectangle is: {sq.rectangle(side_rect_a, side_rect_b)}")
elif figure == 2:
    side_trian_a = float(input("Input side a: "))
    side_trian_b = float(input("Input side b: "))
    side_trian_c = float(input("Input side c: "))
    print(f"The square of the triangle is: {sq.triangle(side_trian_a, side_trian_b, side_trian_c)}")
elif figure == 3:
    rad_cir = float(input("Input circle radius: "))
    print(f"The square of the circle is: {sq.circle(rad_cir)}")