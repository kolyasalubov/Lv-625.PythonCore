import random

class Ghost(object):
    # your code goes here
    def __init__(self) -> None:
        self.color = random.choice(["white", "yellow", "purple", "red"])

ghost = Ghost()
print(ghost.color)