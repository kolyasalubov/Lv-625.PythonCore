# Поміняти між собою значення двох змінних, не використовуючи третьої змінної.
print("Спосіб №1")
a = 5
b = 7
print(f'a = {a}')
print(f'b = {b}')

a = a + b
b = a - b
a = a - b

print("""
a = a + b = 12
b = a - b = 5
a = a - b = 7
""")

print(f'a = {a}')
print(f'b = {b}')

print("""
Спосіб №2""")
c = 8
d = 4
print(f'c = {c}')
print(f'd = {d}')
c, d = d, c
print("c, d = d, c")
print(f'c = {c}')
print(f'd = {d}')