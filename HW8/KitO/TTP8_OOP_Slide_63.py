"""
Create a Car class with the 
attributes: name, kind, model
and methods of start and stop, 
which indicate information that the car started or stoped accordingly.
"""

class Car:
    def __init__(self, name, kind, model):
        self.name = name
        self.kind = kind
        self.model = model

    def start(self):
        return f"{self.name} {self.model} started." 

    def stop(self):
        return f"{self.name} {self.model} stoped."

car_1 = Car("Nissan", "crossover", "Qashqai")
print(f'We have a {car_1.kind} {car_1.name} {car_1.model}.')
print(car_1.start())
print(car_1.stop())



