def login():
    login=input("Please enter your login: ")
    while login!="First":
        print(f"'{login}' is not a valid login!")
        login=input("please enter valid login: ")
        continue
    else:
        print("Hello, welcome to the system!")

login()