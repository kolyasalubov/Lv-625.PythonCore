# In the range from 1 to 10 determine
# even numbers that are divisible by 2,
# odd numbers, which are divisible by 3,
# numbers that are not divisible by 2 and 3.

for i in range(1, 11):
    if i % 2 == 0:
        print(f'{i} is even')
    elif i % 3 == 0:
        print(f'{i} is odd')
    else:
        print(f'{i} are not divisible by 2 and 3')
        