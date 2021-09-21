
number = list(map(int, input('Enter your number: ')))
#1
number.reverse()
print('Reverse number:',''.join(map(str, number)))
#2
sum = 0
for i in number:
    sum += i
print(f'Sum of digits of the number: {sum}')
#3
number.sort()
print('Sorted number:',''.join(map(str, number)))