fib_1 = fib_2 = 1

num = int(input("Input your number: "))

print(fib_1, fib_2, end = ' ')
for i in range(2, num):
    fib_1, fib_2 = fib_2, fib_1 + fib_2
    num -= 1
    print(fib_2, end = ' ')