##### Python Object-Oriented Programming (slide 81)
"""
Create an employee class. 
Each employee has characteristics such as name and salary. 
The class should have a counter that calculates the total number of employees, 
as well as a method that prints the total number of employees 
and a method that displays information about each employee in particular, namely the name and salary.

In addition to creating a class, display information about the base classes 
from which the employee class is inherited (__base__), the class namespace (__dict__), 
the class name (__name__), the module name in which the class is defined (__module__), 
the documentation bar ( __doc__)
"""

class Employee:
    """
    This class contains name and salary of each employee.
    It also counts the total number of employees.
    """
    counter = 0
    def __init__(self, name, salary):
        Employee.counter += 1
        self.name = name
        self.salary = salary

    def __del__(self):
        Employee.counter -= 1

    def total_number_of_employees():
        """
        This function prints the total number of employees.
        """
        print(Employee.counter)

    def employee_info(self):
        """
        This function displays information about each employee (the name and salary).
        """
        return f'{self.name} {self.salary}'

empl_20200415 = Employee ("Tatiana", 90000)
empl_20210215 = Employee ("Sergii", 120000)
empl_20210406 = Employee ("Olga", 100000)
empl_20210906 = Employee ("Oleksandr", 75000)

Employee.total_number_of_employees()

print(empl_20200415.employee_info())
print(empl_20210215.employee_info())
print(empl_20210406.employee_info())
print(empl_20210906.employee_info())

print(Employee.__doc__)
print(Employee.__base__)        # <class 'object'>
print(Employee.__dict__)
print(Employee.__name__)        # Employee
print(Employee.__module__)      # __main__
