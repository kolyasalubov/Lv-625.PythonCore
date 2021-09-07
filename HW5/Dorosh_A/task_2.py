list_numbers = list(range(1, 11))

for i in list_numbers:
    if i % 2 == 0 and i >=2:
        print(f"{i} - even number that are divisible by 2 ")

for i in list_numbers:
    if i % 3 == 0 and i % 2 != 0:
        print(f"{i} -  odd numbers that are divisible by 3 ")
for i in list_numbers:
    if i % 2 != 0 and i % 3 != 0:
        print(f"{i} - number that are not divisible by 2 and 3 ")
