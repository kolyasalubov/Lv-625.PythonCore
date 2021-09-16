# Write a script that will calculate the factorial of the entered number  without using recursion.

input_number = int(input("Input your number: "))
factorial = 1
for i in range(2, input_number + 1):
    factorial *= i

print(f'Factorial of number {input_number} is {factorial}')
