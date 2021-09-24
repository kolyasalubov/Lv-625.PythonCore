class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
    
    def inputSides(self):
        self.sides = [float(input(f"Enter side {str(i+1)}: ")) for i in range(self.n)]

class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)

    def calculate_squadre(self):
        a, b = self.sides
        area = a * b
        print(f"The area of triangle is {area}")

my_triangle = Rectangle()
my_triangle.inputSides()
my_triangle.calculate_squadre()
