class Polygon():
    """
    class polygon is a superclass
    for all polygonal figures
    """
    def __init__(self, num_of_sides):
        self.num_of_sides = num_of_sides
        self.sides = [0 for i in range(num_of_sides)]

    def input_sides(self):
        self.sides = [float(input("Enter side " + str(i + 1) + " : "))
                      for i in range(self.num_of_sides)]


class Rectangle(Polygon):
    """
    class rectangle is subclass of superclass polygon
    will calculate the square of the rectangle
    """
    def __init__(self):
        Polygon.__init__(self, 2)

    def find_square(self):
        a, b = self.sides
        square = a * b
        print(f'The square of rectangle is {square}')

r = Rectangle()
r.input_sides()
r.find_square()
