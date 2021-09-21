import square_of_figures as sqr

figure_name = True
while figure_name:
    figure = input("Do you need to calculate the square of rectangle, triangle or circle?")
    if figure == "rectangle":
        print("Please indicate the sides of the figure!:)")
        a, b = int(input("Enter a:")), int(input("Enter b:"))
        print(f'The square of {figure} =', sqr.s_rectangle(a,b))
        figure_name = False
    elif figure == "triangle":
        print("Please indicate the sides of the figure!:)")
        a, h = int(input("Enter any side:")), int(input("Enter height:")),
        print(f'The square of {figure} =', sqr.s_triangle(a,h))
        figure_name = False
    elif figure =="circle":
        r = int(input("Enter the radius:"))
        print(f'The square of {figure} =', sqr.s_circle(r))
        figure_name = False
    else:
        print("Wrong input. Please, try again.")
        figure_name = True