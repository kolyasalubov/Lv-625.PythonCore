our_number = int(input("insert nomber "))
fib_number1 = 0
fib_number2 = 1
fib_list = None
while our_number > fib_number2:
    if fib_number1 == 0:
        print(fib_number1)
        print(fib_number2)
    else:
        print(fib_number2)
    fib_number2 += fib_number1
    fib_number1 = fib_number2 - fib_number1
