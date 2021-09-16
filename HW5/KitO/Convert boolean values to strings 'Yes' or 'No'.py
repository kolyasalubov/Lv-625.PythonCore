##### https://www.codewars.com/kata/convert-boolean-values-to-strings-yes-or-no
"""
Complete the method that takes a boolean value 
and return a "Yes" string for true, or a "No" string for false.
"""

def bool_to_word(boolean):
    """
    This function converts boolean values to strings 'Yes' or 'No'
    """
    if boolean == 1:
        return "Yes"
    else:
        return "No"

print(bool_to_word(True))   # Yes
print(bool_to_word(False))  # No

######### Інший спосіб:
def bool_to_word2(boolean):
    return "Yes" if boolean else "No"

print(bool_to_word2(True))
print(bool_to_word2(False))