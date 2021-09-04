print("Version 1")
divisible_to_two = []
divisible_to_three = []
not_divisible = []
for i in range(1,11):
    if i % 2 == 0 or i % 3 == 0:
        if i % 2 == 0:
            divisible_to_two.append(i)
        if i % 3 == 0:
            divisible_to_three.append(i)
        continue
    not_divisible.append(i)

print(f"divisible by two = {divisible_to_two}")
print(f"divisible by tree = {divisible_to_three}")
print(f"not divisible by two and by three = {not_divisible}")

print("\nVersion 2")
divisible_to_two = []
divisible_to_three = []
not_divisible = []
for i in range(1,11):
    if i % 2 == 0:
        divisible_to_two.append(i)
    if i % 3 == 0:
        divisible_to_three.append(i)
    if i % 2 != 0 and i % 3 != 0:
        not_divisible.append(i)

print(f"divisible by two = {divisible_to_two}")
print(f"divisible by tree = {divisible_to_three}")
print(f"not divisible by two and by three = {not_divisible}")

print("\nVersion 3")
divisible_to_two = [i for i in range(1,11) if i % 2 == 0]
divisible_to_three = [i for i in range(1,11) if i % 3 == 0]
not_divisible = [i for i in range(1,11) if i % 2 != 0 and i % 3 != 0]

print(f"divisible by two = {divisible_to_two}")
print(f"divisible by tree = {divisible_to_three}")
print(f"not divisible by two and by three = {not_divisible}")

print("\nVersion 4")
for i in range(1,11):
    print(f"{i} is not_divisible by two and by three" if i % 2 != 0 and i % 3 != 0 else (f"{i} is divisible by two and by three" if i % 3 == 0 and i % 2 == 0 else\
        (f"{i} is divisible by two" if i % 2 == 0 else f"{i} is divisible by tree")))
