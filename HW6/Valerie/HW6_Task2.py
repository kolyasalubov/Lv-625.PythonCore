from math import pi

def s_rectangle(a,b):
    return round(a*b, 2)

def s_triangle(a,b,c):
    p = 0.5 * (a + b + c)
    s_triangle = (p*(p-a)*(p-b)*(p-c))**0.5
    return round(s_triangle, 2)

def s_circle(r):
    s_circle = pi*(r**2)
    return round(s_circle, 2)

figure_name = True
while figure_name:
    figure = input("Do you need to calculate the square of rectangle, triangle or circle?")
    if figure == "rectangle":
        print("Please indicate the sides of the figure!:)")
        a, b = int(input("Enter a:")), int(input("Enter b:"))
        print(f'The square of {figure} =', s_rectangle(a,b))
        figure_name = False
    elif figure == "triangle":
        print("Please indicate the sides of the figure!:)")
        a, b, c = int(input("Enter a:")), int(input("Enter b:")), int(input("Enter c:"))
        print(f'The square of {figure} =', s_triangle(a,b,c))
        figure_name = False
    elif figure =="circle":
        r = int(input("Enter the radius:"))
        print(f'The square of {figure} =', s_circle(r))
        figure_name = False
    else:
        print("Wrong input. Please, try again.")
        wrong_input = True