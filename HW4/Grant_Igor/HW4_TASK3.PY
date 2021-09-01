number = int(input("Choose a number for the Fibonacci sequence! "))
fibonacci_numbers = [0, 1]
for i in range(2, number):
    fibonacci_numbers.append(fibonacci_numbers[i-1] + fibonacci_numbers[i-2])
print(f"Sequence in range: {fibonacci_numbers}")
