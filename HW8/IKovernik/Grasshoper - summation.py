import re

def validate():
    while True:
        password = input("Enter a password: ")
        if len(password) < 6 or len(password)>16:
            print("Make sure your password is 6-16 letters length")
        elif re.search('[0-9]',password) is None:
            print("Make sure your password has a number in it")
        elif re.search('[A-Z]',password) is None or re.search('[a-z]',password) is None: 
            print("Make sure your password includes small [a-z], and captual [A-Z] letters")
        else:
            print("Your password seems fine")
            break

validate()