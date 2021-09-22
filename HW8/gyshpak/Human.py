class Homosapiens():
    def __init__(self, age, sex) -> None:
        self.age = age
        self.sex = sex

    def stat_metod():
        print("Homosapients like San")
        
        
class Human(Homosapiens):
    def __init__(self, name, age, sex) -> None:
        super().__init__(self, age, sex)
        self.name = name
        # self.age = age
        # self.sex = sex
       
    def metod_classa(cls):
        print("This metod of class")

    def about_Human(self):
        print(f"My name is {self.name}, age = {super.age}, sex is {super.sex}")

Human1 = Human("Gena", "45", "Man")

Human1.about_Human()

