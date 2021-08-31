# Поміняти між собою значення двох змінних, не використовуючи третьої змінної.
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