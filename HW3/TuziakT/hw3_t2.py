"""
for the resolving of this tusk we need to use 3 methods
before all of that i like more when you can giv your own number
now about methods:
1-st metod is about reversing of your number
2-nd metod is about product(sum) of numbers
3-d metod is about sort the numbers that are in your number
"""
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