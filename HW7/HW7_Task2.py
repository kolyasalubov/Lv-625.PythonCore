def passwword_function():
    password = input("Password: ")
    for symbol in password:
        if symbol in letter_range ("a", "z"):
            return password
    #         symbol in letter_range ("A", "Z")
    #
    #
    #
    # else:
    #     return ("Please check oyur password again!")


