class Human:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def static():
        return "This is static method"    

    def homo(self):
        print(f"{self.name} is Homosapiens")
    
    def hello(self):
        print(f"Hello {self.name}")


victor = Human("Victor")
victor.hello()
victor.homo()
print(Human.static())
