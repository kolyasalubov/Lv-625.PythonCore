number = int(input("Enter number for Fibonacci list "))
fib=[0,1]
if number == 0:
    print(f"Fibonacci list  of your entrede number {number} is [0]")
elif number == 1:
    print(f"Fibonacci list  of your entrede number {number} is {fib}")
elif number < 0:
    print(f"{number} is negative number, please enter positive number")
else:
    for i in range(1, number):
        fib.append(fib[i-2]+fib[i-1])
        print(f"number  {i} in Fibonacci list is {(fib[i-2]+fib[i-1])}")
    print(f'Fibonacci list  of your entrede number {number} is {fib}')

