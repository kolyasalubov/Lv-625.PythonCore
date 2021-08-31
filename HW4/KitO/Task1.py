# Write a script that will calculate the factorial of the entered number without using recursion.

customer_number = int(input('Enter your number: '))
print(f'Your number is: {customer_number}')
factorial = 1

if customer_number in (0,1):
    factorial = 1
else:
    for n in range(2,customer_number+1):
        factorial = factorial * n
print(f'The factorial of the entered number is {factorial}')
