class Polygon:
    def __init__(self, sides_for_square):
        self.sides = sides_for_square    
    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.sides)]

class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2) 
    def square_calculation(self):
        len, hei = self.sides
        print("The square of rectangle is: ", len*hei)

p = Rectangle()
p.inputSides()
p.square_calculation()