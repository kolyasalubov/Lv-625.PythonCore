class Emploees:
    my_count = 0
    def __init__(self, name, salary):
        self.name = name
        self. salary = salary
        Emploees.my_count += 1

    @staticmethod
    def stat_method():
        return "Static metod"

    def return_prop(self):
        print(f"My name is {self.name}, my salary = {self.salary}")
    
    @classmethod
    def print_count(slc):
        print(f"Count of emploees is {Emploees.my_count}")
    

Emp1 = Emploees('Gege1', 11000)
Emp2 = Emploees('Gege2', 12000)
Emp3 = Emploees('Gege3', 13000)
Emp4 = Emploees('Gege4', 14000)
Emp5 = Emploees('Gege5', 15000)

Emploees.print_count()
Emp1.return_prop()
print(Emploees.stat_method())
print(Emploees(__))