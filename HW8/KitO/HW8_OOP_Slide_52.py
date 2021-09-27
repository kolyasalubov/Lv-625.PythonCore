##### Python Object-Oriented Programming (slide 52)
"""
Create a polygon class and a rectangle class 
that inherits from the polygon class and finds the square of rectangle.
"""

class Polygon:
    def __init__(self, num_of_sides):
        self.n = num_of_sides
        self.sides = [0 for i in range(num_of_sides)]   # готуємо контейнер для значень сторін

    def inputSides(self):
        # створюємо сторони (конструкція List Comprehension)
        self.sides = [float(input(f"Enter side {i+1}: ")) for i in range(self.n)]
        
    def dispSides(self):    # переглядаємо сторони
        for i in range(self.n):
            print(f"Side {i+1} is {self.sides[i]}")

class Triangle(Polygon):
    def __init__(self):
        # Polygon.__init__(self,3)  
        super().__init__(3) 

    def findArea(self):
        a, b, c = self.sides
        # розраховуємо напівпериметр
        s = (a + b + c) / 2
        # шукаємо площу за формулою Герона
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print(f'The area of the triangle is {area}')

class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)
    
    def findArea(self):
        a, b = self.sides
        area = a * b
        print(f'The area of the rectangle is {area}')

r = Rectangle()
r.inputSides()
r.dispSides()
r.findArea()



