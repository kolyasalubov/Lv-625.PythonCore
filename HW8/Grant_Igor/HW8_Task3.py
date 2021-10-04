class Employee():
    """
    class employee will have attributes such as
    name and salary, will count the amount of employees
    and return the number
    """
    emp_counter = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_counter += 1
    def count_of_emp(self):
        """
        returns the number of employees
        """
        return f"The number of employees is {Employee.emp_counter}"
    def show_info(self):
        """
        returns employee’s name and salary
        """
        return f"Name - {self.name}, salary - {self.salary} \n"
emp1 = Employee("Joe", 3500)
emp2 = Employee("Alex", 7500)
emp3 = Employee("Stephan", 100500)

print(emp1.show_info(), emp2.show_info(), emp3.show_info())
print("Number of employees: ", Employee.emp_counter)
print(emp1.__dict__)
print(emp1.__doc__)
print(emp1.__module__)
print(emp1.__name__) # Doesnt show any info
print(emp1.__base__) # Doesnt show any info