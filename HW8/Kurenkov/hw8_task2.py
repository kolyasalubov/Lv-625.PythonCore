# Create a class Human, everyone has a name, create a method in the class that displays a welcome message to a each person.
# Create a class method in the class that returns information that it is a species of "Homosapiens"
# And also in the class create a static method that returns an arbitrary message.

class Human:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def description():
        return f'In this class Greet and Species methods operate with name only'

    @classmethod
    def speceis(cls):
        return f'{cls} belongs to the Homosapiens species'

    def greet(self):
        return f'Hello {self.name}'


print(Human.description())
person = Human("Jenny")
print(person.description())

print(person.greet())
print(person.speceis())
