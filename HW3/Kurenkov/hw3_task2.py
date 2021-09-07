# Задано чотирицифрове натуральне число.
# - Знайти добуток цифр цього числа.
# - Записати число в реверсному порядку.
# - Посортувати цифри, що входять в дане число


input_number = input("Input your number: ")
if input_number.isdigit():
    product_num = eval('*'.join(input_number))
    reverse_num = ''.join(sorted(input_number, reverse=True))
    sorted_num = ''.join(sorted(input_number))
    print(f'Product of your number is {product_num}, sorted is {sorted_num}, and reversed is {reverse_num}')
else:
    print("Try another input")


