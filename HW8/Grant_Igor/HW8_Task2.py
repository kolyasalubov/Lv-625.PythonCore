class Homosapiens():
    def __init__(self, species="homosapiens"):
        self.species = species
    def hms(self):
        return ("Your species is " + self.species)
class Human(Homosapiens):
    def __init__(self, name, you_are="human"):
        self.you_are = you_are
        self.name = name
        print("Hello " + self.name)
        Homosapiens.__init__(self)
    def info(self):
        return (self.name + ", you are " + self.you_are + ". Your species is " +self.species)
    @staticmethod
    def fucntion():
        return ("Static method message")
me = Human("Igor")
print(me.info())
print(Human.fucntion())
