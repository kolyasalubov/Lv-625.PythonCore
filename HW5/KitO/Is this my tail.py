##### https://www.codewars.com/kata/is-this-my-tail/train/python
"""
Some new animals have arrived at the zoo. 
The zoo keeper is concerned that perhaps the animals do not have the right tails. 
To help her, you must correct the broken function to make sure that the second argument (tail), 
is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!

If the tail is right return true, else return false.

The arguments will always be strings, and normal letters.

For Haskell, body has the type of String and tail has the type of Char. 
For Go, body has type string and tail has type rune.
"""

def correct_tail(body, tail):
    sub = body.substr(len(body)-len(tail.length)
    # if sub = tai:
    #     return True
    # else: #to do
    #     return False

