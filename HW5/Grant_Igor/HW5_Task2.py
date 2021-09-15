login = input("Enter username: ")
while login != "First":
    print("Error, try again!")
    login = input("Enter username: ")
else:
    print(f"Welcome {login}")

