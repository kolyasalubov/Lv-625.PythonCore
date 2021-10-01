"""
Classy Classes
Basic Classes, this kata is mainly aimed at the new JS ES6 Update introducing classes
Task
Your task is to complete this Class, the Person class has been created. You must 
fill in the Constructor method to accept a name as string and an age as number,
 complete the get Info property and getInfo method/Info getter which should return 'johns age is 34'
"""




class Person:
    def __init__(self, name = input("Enter name "), age = int(input("Enter age "))):
        self.name = name
        self.age = age
    def getInfo(self):
        return f"{self.name} age  is a {self.age}"
print(Person().getInfo())