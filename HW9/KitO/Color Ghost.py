##### https://www.codewars.com/kata/color-ghost
"""
Create a class Ghost
Ghost objects are instantiated without any arguments.
Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated

ghost = Ghost()
ghost.color  => "white" or "yellow" or "purple" or "red"
"""

class Ghost(object):
    def __init__(self):
        import random
        color_list = ["white", "yellow", "purple", "red"]
        self.color = random.choice(color_list)
        print(self.color)
            
ghost1 = Ghost()
ghost2 = Ghost()


