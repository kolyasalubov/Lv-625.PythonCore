number = 3791
product_of_a_number = 1
list_of_numbers = []
while number > 0:
    modulus_of_number = number % 10
    product_of_a_number *= modulus_of_number
    number //= 10
    list_of_numbers.append(modulus_of_number)
print(product_of_a_number)
print(*list_of_numbers, sep='')
sorted_list = sorted(list_of_numbers)
print(*sorted_list, sep='')