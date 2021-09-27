##### Python Object-Oriented Programming (slide 72)
"""
Create a class Human, everyone has a name, 
create a method in the class that displays a welcome message to a each person. 
Create a class method in the class that returns information 
that it is a species of "Homosapiens". 
And also in the class create a static method that returns an arbitrary message. 
"""

class Human:
    def __init__(self, name):
        self.name = name
    
    def welcome(self):
        return f"Welcome {self.name}"
    
    @classmethod
    def species(cls):
        return 'Homosapiens', cls

    @staticmethod
    def count_humans():
        return 'The world population of humans was 7,800,000,000 people as of March 2020.'

human1 = Human("Adam")
human2 = Human("Eva")

print(human1.welcome())
print(human2.welcome())
print(Human.species())
print(Human.count_humans())
