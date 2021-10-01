"""
Create an employee class. Each employee has characteristics such as name and salary. 
The class should have a counter that calculates the total number of employees, as well as 
a method that prints the total number of employees and a method that displays information 
about each employee in particular, namely the name and salary.

In addition to creating a class, display information about the base classes from which the
 employee class is inherited (__base__), the class namespace (__dict__), the class name 
 (__name__), the module name in which the class is defined (__module__), 
 the documentation bar ( __doc__) 

"""
class Employee:
    num_counter = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.num_counter +=1
    def count_employee(self):
        return f"The number of employees {Employee.num_counter}"
    def info_of_employee(self):
        return f"\n The employee  {self.name} has salary {self.salary}"
employee1 = Employee("Andrii", 4000)
employee2 = Employee("Mary", 6000)
employee3 = Employee("Oksana", 1000)
employee4 = Employee("Roman", 2000)


print(employee1.info_of_employee(), employee2.info_of_employee(),
employee3.info_of_employee(), employee4.info_of_employee())
print(employee4.count_employee())
print(f"Base classe is {Employee.__base__}")
print(f"Class namespace: {Employee.__dict__}")
print(f"Name class is {Employee.__name__}")
print(f"Module name in which the class: {Employee.__module__}")
print(f"Documentation bar: {Employee.__doc__}")
