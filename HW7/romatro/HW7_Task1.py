import geometric_shapes as g

selected_shape=input("please type the name of shape for which square must be calculated: ")

if selected_shape=="triangle":
    print("triangle square equals: "+str(g.triangle_square()))
elif selected_shape=="rectangle":
    print("rectangle square equals: "+str(g.rectangle_square()))
elif selected_shape=="circle":
    print("circle square equals: "+str(g.circle_square()))
else:
    print(f"selection '{selected_shape}' is not a valid option, please enter one of the valid options: triangle, rectangle or circle")
