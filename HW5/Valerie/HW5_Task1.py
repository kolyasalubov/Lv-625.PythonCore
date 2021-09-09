even_numbers, odd_numbers, not_divisible_numbers = [], [], []
for i in range(1,11):
    if i%2 == 0:
        even_numbers.append(i)
    elif i%3 == 0:
        odd_numbers.append(i)
    elif i%2 != 0 and i%3 != 0:
        not_divisible_numbers.append(i)
print(*even_numbers)
print(*odd_numbers)
print(*not_divisible_numbers)
