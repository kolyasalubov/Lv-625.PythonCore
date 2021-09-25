class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        return f"{self.name} is {self.age} y.o"
p = Person("Alex", 25)
print(p.info())
