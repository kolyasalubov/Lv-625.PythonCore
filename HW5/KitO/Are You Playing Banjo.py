##### https://www.codewars.com/kata/are-you-playing-banjo
"""
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

name + " plays banjo" 
name + " does not play banjo"

Names given are always valid strings.
"""

def are_you_playing_banjo(name):
    if name[0].upper() == "R":
        return name + " plays banjo"
    return name + " does not play banjo"

def are_you_playing_banjo2(name):
    if name[0].lower() == "r":
        return name + " plays banjo"
    return name + " does not play banjo"

print(are_you_playing_banjo("martin"))
print(are_you_playing_banjo("Rikke"))
print(are_you_playing_banjo("royc"))
print(are_you_playing_banjo2("Rikke"))
print(are_you_playing_banjo2("royc"))
