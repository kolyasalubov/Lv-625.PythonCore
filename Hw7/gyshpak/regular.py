import re

my_string = '88888888'
my_match = re.fullmatch(r'[(a-z)+(A-Z)+(0-9)+]{6,8}', my_string)
# my_match = re.fullmatch(r'[a-zA-Z0-9]{6,16}', my_string)
# my_match = re.fullmatch(r'([a-z]+[A-Z]+[0-9]+[$#@]+){6-16}', my_string)
print('YES' if my_match else 'NO')
