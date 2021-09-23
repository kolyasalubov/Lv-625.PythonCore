class Polygon():
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides
        self.sides = [0 for i in range(number_of_sides)]

    def input_sides(self):
        self.sides = [float(input(f"Enter side {str(i + 1)}: "))
                      for i in range(self.number_of_sides)]

    def show_sides(self):
        for i in range(self.number_of_sides):
            print(f"Side {i + 1} is {self.sides[i]}")


# class Rectangle(Polygon):
#     def __init__(self):
#         super().__init__(self)
#     def squere(self):
#         a, b = self.sides
#         sqr = a * b
#         return sqr
# r = Rectangle()
# r.squere()

r = Polygon()
r.input_sides()
r.show_sides()
