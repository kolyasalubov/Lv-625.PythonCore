def triangle_square():
    base=int(input("please enter triangle base: "))
    height=int(input("please enter triangle height: "))
    sq_tri=1/2*(base*height)
    print("the square of a triangle = "+str(sq_tri))

def rectangle_square():
    width=int(input("please enter rectangle width: "))
    height=int(input("please enter rectangle height: "))
    sq_rect=(width*height)
    print("the square of a rectangle = "+str(sq_rect))

def circle_square():
    radius=int(input("please enter circle radius: "))
    PI=3.141592653589793
    sq_circle=PI*radius**2
    print("the square of a circle = "+str(sq_circle.__round__(2)))

# import geometric_shapes as g

selected_shape=input("please type the name of shape for which square must be calculated: ")

if selected_shape=="triangle":
    triangle_square()
elif selected_shape=="rectangle":
    rectangle_square()
elif selected_shape=="circle":
    circle_square()
else:
    print(f"selection '{selected_shape}' is not a valid option, please enter one of the valid options: triangle, rectangle or circle")