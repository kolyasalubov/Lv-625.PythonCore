number = list(map(int, input('Enter your number: ')))

sum = 0
for i in number:
    sum += i
print(f'Sum of digits of the number: {sum}')

number.reverse()
print('Reverse number:',''.join(map(str, number)))

number.sort()
print('Sorted number:',''.join(map(str, number)))