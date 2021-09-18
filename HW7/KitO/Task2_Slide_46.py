##### Slide_45
##### Write a Python program to check the validity of a password (input from users).

import re

password = input("Enter your password: ")       # !February2021@!February2021@

def checkPass (password):
    """
    This function checks the validity of a password.
    Validation :
    At least 1 letter between [a-z] and 1 letter between [A-Z].
    At least 1 number between [0-9].
    At least 1 character from [$#@].
    Minimum length 6 characters.
    Maximum length 16 characters.
    """
    check1 = re.findall("[a-z]", password)
    check2 = re.findall("[A-Z]", password)
    check3 = re.findall("[0-9]", password)
    check4 = re.findall("[$|#|@]", password)
    check5 = len(password) >= 6
    check6 = len(password) <= 16
    if check1 and check2 and check3 and check4 and check5 and check6:
        print("Your password is secure.")
    else:
        print("Your password is not secure. Try again.")

checkPass(password)

