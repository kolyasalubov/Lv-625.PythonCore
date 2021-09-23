class Human():
    """
    This is superclass 'human'
    it is going to have certain amount of subclasses
    according to the need of a program
    """
    def __init__(self, species="human"):
        self.species = species
    def res(self):
        return ("I am " + self.species)

class Man(Human):
    """
    This is subclass 'man', will inherit superclass 'human'
    """
    def __init__(self, name, gender="man"):
        self.name = name
        self.gender = gender
        Human.__init__(self, species="human")
    def gen_man(self):
        return ("I am " + self.species + ". My name is " + self.name + " and I am a " + self.gender)

class Woman(Human):
    """
    This is subclass 'woman', will inherit superclass 'human'
    """
    def __init__(self, name, gender="woman"):
        self.name = name
        self.gender = gender
        Human.__init__(self, species="human")
    def gen_woman(self):
        return ("I am " + self.species + ". My name is " + self.name + " and I am a " + self.gender)

woman = Woman("Eve")
man = Man("Adam")

def god():
    """
    Function is using the information provided from prevoius
    subclasses such as 'Man' and "Woman'
    returning the information about chosen individuals
    """
    return (woman.gen_woman(), man.gen_man())
print(god())

