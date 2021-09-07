number=int(input('Enter number '))
factorial = 1
if number == 0 or number == 1:
    print(f"{number}!= {factorial}")

elif number < 0:
    print(f"{number} is negative number, please enter positive number")
else:
    for count in range(2, number+1):
        factorial *= count
    print(f"{number}!= {factorial}")

