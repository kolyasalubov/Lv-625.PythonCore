# Записати в стрічку філософію Пайтона
# - Знайти в заданій стрічці кількість
#   входжень слів (better, never, is)
# - Вивести весь текст у верхньому регістрі (всі великі літери)
# - Замінити всі входження символу “і” на “&”

import sys

temp = sys.stdout
sys.stdout = open('zen.txt', 'w')

import this

sys.stdout.close()
sys.stdout = temp

file = open('zen.txt')
zen = file.read()
words_to_count = ['better', 'never', 'is']
for i in words_to_count:
    print(f"The word '{i}' occurs {zen.find(i)} times")

print(zen.upper())
print(zen.replace('i', '&'))


