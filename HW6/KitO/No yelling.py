##### https://www.codewars.com/kata/no-yelling
"""
Write a function taking in a string like WOW this is REALLY amazing 
and returning Wow this is really amazing. 
String should be capitalized and properly spaced. 
Using re and string is not allowed.
"""

def filter_words(st):
    u = st[1:].lower()
    St = st[0].upper()
    return St + u

print(filter_words('HELLO CAN YOU HEAR ME'))   # Hello can you hear me
print(filter_words('now THIS is REALLY interesting'))   # Now this is really interesting
print(filter_words('THAT was EXTRAORDINARY!'))   # That was extraordinary!

