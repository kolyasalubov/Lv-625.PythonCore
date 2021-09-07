# Print Fibonacci numbers up to the entered number n,
# using cycles.
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)

fibo_input = int(input("Input your number: "))
fibo_sequence = [0, 1]
for i in range(2, fibo_input):
        fibo_sequence.append(fibo_sequence[i-1] + fibo_sequence[i-2])
print(fibo_sequence)
