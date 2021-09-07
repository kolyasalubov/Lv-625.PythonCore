###### https://www.codewars.com/kata/55225023e1be1ec8bc000390
"""
Jenny has written a function that returns a greeting for a user. 
However, she's in love with Johnny, and would like to greet him slightly different. 
She added a special case to her function, but she made a mistake.
"""

def greet(name):
    while name != "Johnny":
        return "Hello, {name}!".format(name=name)
    else:
        return "Hello, my love!"

print(greet("Olga"))
print(greet("Johnny"))