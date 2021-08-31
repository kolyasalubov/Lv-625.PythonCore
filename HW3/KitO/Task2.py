# Задано чотирицифрове натуральне число. 
# Знайти добуток цифр цього числа.
# Записати число в реверсному порядку.
# Посортувати цифри, що входять в дане число.

natural_number = 1973
print(f'Ваше число = {natural_number}')
list_of_numbers = list(str(natural_number))
list_of_numbers_with_sep = '*'.join(list_of_numbers)
the_product_of_numbers = eval(list_of_numbers_with_sep)
print(f'Добуток цифр = {the_product_of_numbers}')

# Спосіб 1
# reverse_list = list_of_numbers.reverse()
# reversed_numbers = int(''.join(list_of_numbers))
# print(f'Число у реверсному порядку = {reversed_numbers}')
# Спосіб 2
print(f'Число у реверсному порядку = {"".join(reversed(list_of_numbers))}')
# Спосіб 3
print(f'Число у реверсному порядку = {int("".join(list(str(natural_number))[::-1]))}')

# Спосіб 1
sorted_list = list_of_numbers.sort()
sorted_numbers = int(''.join(list_of_numbers))
print(f'Відсортовані цифри = {sorted_numbers}')
# Спосіб 2
print(f'Відсортовані цифри = {"".join(sorted(list_of_numbers))}')