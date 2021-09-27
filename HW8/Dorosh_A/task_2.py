"""
Create a class Human, everyone has a name, create a method in the class that displays 
a welcome message to a each person. Create a class method in the class that returns 
information that it is a species of "Homosapiens". And also in the class create a 
static method that returns an arbitrary message. 

"""
class Human:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
    def welcomeMsg(self):
        print(f"Welcome {self.name},  your sex  is {self.sex}")
    @classmethod
    def ClassMethod(cls):
        print(f"It is a species of 'Homosapiens' ")
    @staticmethod
    def StaticMethod():
        print (f"Condratulation ")

name = input("Enter your name ")
sex = input(" Enter specify your gender ")
r = Human(name, sex)
r.welcomeMsg()
r.ClassMethod()
r.StaticMethod()
