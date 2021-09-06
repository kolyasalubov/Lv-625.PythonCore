numbers_divisible_two = []
numbers_divisible_three = []
numbers_not_divisible = []

for i in range(1, 11):
    if i%3 == 0 and i%2 == 0:
        numbers_divisible_two.append(i)
        numbers_divisible_three.append(i)
    elif i%2 == 0:
        numbers_divisible_two.append(i)
    elif i%3 == 0:
        numbers_divisible_three.append(i)
    elif i%3 != 0 and i%2 != 0:
        numbers_not_divisible.append(i)

print(numbers_divisible_two)
print(numbers_divisible_three)
print(numbers_not_divisible)