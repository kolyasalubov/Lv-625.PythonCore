"""
Create a class Ghost

Ghost objects are instantiated without any arguments.

Ghost objects are given a random color attribute of white" or "yellow" or "purple" or "red" when instantiated

ghost = new Ghost();
ghost.color //=> "white" or "yellow" or "purple" or "red"
"""
import random
class Ghost:
    list_color = ["white", "yellow", "purple", "red" ]
    def __init__(self, random_color=random.choice(list_color)):
        self.random_color = random_color
    def color(self):
        return f"{self.random_color}"

ghost = Ghost()
print(ghost.color())

