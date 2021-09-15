import square as sq
# Imported module will calculate the square of chose figure
figure = int(input("Select the figure for square calculation: 1. Rectangle, 2. Triangle, 3. Circle "))
if figure == 1:
    # Figure one for rectangle
    print(sq.rectangle())
elif figure == 2:
    # Figure two for triangle
    print(sq.triangle())
elif figure == 3:
    # Figure three for circle
    print(sq.circle())
