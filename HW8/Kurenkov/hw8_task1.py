# Create a polygon class and a rectangle class
# that inherits from the polygon class and finds the square of rectangle.

class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side " + str(i + 1) + " : ")) for i in range(self.n)]


class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 2)

    def findArea(self):
        a, b = self.sides
        s = a*b
        print(f'The area of the rectangle is {s}')


d = Rectangle()
d.inputSides()
d.findArea()

