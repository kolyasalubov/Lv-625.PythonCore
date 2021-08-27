our_number = int(input("Insert number "))
our_factorial = 1

if our_number == 1 or our_number == 0:
    our_factorial = 1
else:
    for i in range(1,our_number + 1):
        our_factorial *= i

print(f"Faktorial of number {our_number} = {our_factorial}")