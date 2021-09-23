import square

figure = input("Choose want do you want to do\n"
            "1 - rectangle\n"
            "2 - triangle\n"
            "3 - circle\n")

if figure == "1":
    print(square.rectangle())
elif figure == "2":
    print(square.triangle())
elif figure == "3":
    print(square.circle())  
    