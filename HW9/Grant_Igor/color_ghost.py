import random
class Ghost():
    """
    object of the class 'ghost'
    will get the random color
    out of given list
    """
    def __init__(self):
        colors = ["Green", "Red", "White", "Orange", "Blue"]
        self.color = random.choice(colors)

boo = Ghost()
print("Boo’s color is: ", boo.color)