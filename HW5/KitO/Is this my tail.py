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

def correct_tail(body: str, tail: str) -> bool:
    """
    This function checks if the tail is the same as the last letter(s) of the body.
    """
    n = len(body)-len(tail)
    if body[n:] == tail:
        return bool(1)
    return bool(0)
    
print(correct_tail("Fox", "x")) # True
print(correct_tail("Rhino", "o")) # True
print(correct_tail("Meerkat", "t")) # True
print(correct_tail("Emu", "t")) # False
print(correct_tail("Badger", "s")) # False
print(correct_tail("Giraffe", "fe")) # True

### correct_tail = lambda a, b: a[-1] == b