"""
According to the creation myths of the Abrahamic religions, 
Adam and Eve were the first Humans to wander the Earth.

You have to do God's job. The creation method must return 
an array of length 2 containing objects (representing Adam and Eve). 
The first object in the array should be an instance of the class Man.
The second should be an instance of the class Woman. Both objects have
 to be subclasses of Human. Your job is to implement the Human, Man and Woman classes.
"""
import pprint
class Human:
    def __init__(self, first_man = "Adam", first_woman="Eva") -> None:
        self.first_man=first_man
        self.first_woman=first_woman
class Man(Human):
    def __init__(self, first_man="Adam", first_woman="Eva"):
        super().__init__(first_man=first_man, first_woman=first_woman)

    def firstMan(self):
        return f"First man on Earth was {self.first_man}"
class Woman(Human):
    def __init__(self, first_man="Adam", first_woman="Eva"):
        super().__init__(first_man=first_man, first_woman=first_woman)
    def firstWoman(self):
        return f"First woman on Eart was {self.first_woman}"
def God():
    man=Man().firstMan()
    woman = Woman().firstWoman()
    return f"{man} \n{woman}"
print (God())
