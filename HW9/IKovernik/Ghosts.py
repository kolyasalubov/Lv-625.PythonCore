import random

class Ghost:




    def __init__(self, color=None):
        colors = ['white', 'yellow', 'purple', 'red']
        randomindex = random.randint(0,len(colors)-1) 
        self.color=colors[randomindex]