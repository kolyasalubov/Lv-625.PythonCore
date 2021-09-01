def greet(name):
    if name == "Johnny":
        return "Hello my love!"
    else:
        return "Hello, {}".format(name)
hello = greet(input("Enter your name : "))
print(hello)
