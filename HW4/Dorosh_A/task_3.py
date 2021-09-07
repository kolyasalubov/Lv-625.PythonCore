def pool(name):
    if name == "Johnny":
        return "Hello my love!"
    else:
        return "Hello, {}".format(name)
word = pool(input("Enter your name : "))
print(word)

