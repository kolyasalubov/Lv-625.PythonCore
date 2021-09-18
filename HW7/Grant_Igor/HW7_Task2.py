import re
"""
Password generator for module re
"""
def password_gen_two():
    while True:
        password = input("Enter password: ")
        if len(password) < 6 or len(password) > 16:
            print("Password lenght should be between 6 and 16 symbols")
        elif not re.search("[a-z]", password):
            print("Use lower case letter in range 'a-z'")
        elif not re.search("[A-Z]", password):
            print("Use upper case letter in range 'A-Z'")
        elif not re.search("[0-9]", password):
            print("Use number in range '0-9'")
        elif not re.search("[@#$%^&*()]", password):
            print("Use one of the special symbols '@#$%^&*()'")
        else:
            break
    print("Password accepted")
password_gen_two()
