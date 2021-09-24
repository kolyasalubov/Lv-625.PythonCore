class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    @staticmethod
    def Stat_metod():
        return "This is ststic metod"

    @classmethod
    def Metod_classa(cls):
        print("it is a species of 'Homosapiens'")
    
    def About_human(self):
        print(f"Hellow, my name is {self.name}, age = {self.age}, sex is {self.sex}")


Human1 = Human("Gena", "45", "Man")
Human2 = Human("Olya", "18", "Woan")
Human3 = Human("Vova", "25", "Man")
Human4 = Human("Sveta", "30", "Woman")


Human1.About_human()
Human.Metod_classa()
print(Human.Stat_metod())
Human2.About_human()
Human3.About_human()
Human4.About_human()
