class Car:
    def __init__(self, name, kind, model):
        self.name = name
        self.kind = kind
        self.model = model
    
    def start_car(self):
        print(f"The {self.name} Car is started")
    
    def stop_car(self):
        print(f"The {self.name} Car is stopped")

car1 = Car("Breen", "SUV", "Rav4")
car2 = Car("Dreen", "sedan", "corola")

car1.start_car()
car2.stop_car()