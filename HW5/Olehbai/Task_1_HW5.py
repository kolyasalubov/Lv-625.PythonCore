even_num = [i for i in range(1, 11) if i % 2 == 0]
odd_num = [i for i in range(1, 11) if i % 3 == 0]
num_not_div = [i for i in range(1, 11) if not i % 2 == 0 and not i % 3 == 0]

print("Even numbers that are divisible by 2 {}".format(even_num))
print("Odd numbers that are divisible by 3 {}".format(odd_num))
print("Numbers that are not divisible by 2 and 3 {}".format(num_not_div))

