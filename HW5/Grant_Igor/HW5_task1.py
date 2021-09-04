# Numbers in range of 10 divisible by 2
for i in range(10):
    if i % 2 == 0:
        print(i, end=" ")

# Numbers in range of 10 divisible by 3
for i in range(10):
    if i % 3 == 0:
        print(i, end=" ")

# Numbers in range of 10 that are not divisible by 2 nor 3
for i in range(10):
    if i % 2 != 0 and i % 3 != 0:
        print(i, end=" ")