class Employee:
    emp_counter = 0

    def __init__(self, name, salary):
        Employee.emp_counter += 1
        self.name = name
        self.salary = salary

    def emp_count(self):
        """
        This func returns the numbers of employee
        """ 
        return f"You have {Employee.emp_counter} employees"

    def info_of_emp(self):
        """
        This func returns information about employees
        """
        return f"{self.name} has {self.salary} salary"


emp = Employee("Victor", "1234")

print(emp.info_of_emp())
print("Numbers of employee:", Employee.emp_counter)
print(emp.__dict__)
print(emp.__doc__)
print(emp.__module__)
