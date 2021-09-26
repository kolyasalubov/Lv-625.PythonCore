list_numbers = list(range(1, 11))

for i in list_numbers:
    if i % 2 == 0 and i >=2:
        print(f"{i} - парне число, що ділиться на 2 ")

for i in list_numbers:
    if i % 3 == 0 and i % 2 != 0:
        print(f"{i} -  непарні числа, які діляться на 3 ")

for i in list_numbers:
    if i % 2 != 0 and i % 3 != 0:
        print(f"{i} - числа, які не діляться на 2 і 3 ")