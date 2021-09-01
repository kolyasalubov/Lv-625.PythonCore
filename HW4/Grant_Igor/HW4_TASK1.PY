number = int(input("Enter your number : "))
factorial = 1
if number<0:
    print("Enter positive number!")
else:
    for i in range(1, number+1):
        factorial *= i
    print(f"Factorial = {factorial}")
