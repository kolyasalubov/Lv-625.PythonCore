# Записати в стрічку філософію Пайтона 
# Знайти в заданій стрічці кількість входжень слів (better, never, is)
# Вивести весь текст у верхньому регістрі (всі великі літери)
# Замінити всі входження символу “і” на “&”

import this
import codecs
zen_of_python_str = codecs.encode(this.s, 'rot13') # https://stackoverflow.com/questions/23794344/how-can-i-return-pythons-import-this-as-a-string
print(" ")

print(f'The word "better" appears in The Zen of Python {zen_of_python_str.count("better")} times.')
print(f'The word "never" appears in The Zen of Python {zen_of_python_str.count("never")} times.')
print(f'The word "is" appears in The Zen of Python {zen_of_python_str.count("is")} times.')
print(" ")

print(f'{zen_of_python_str.upper()}')
print(" ")

print(f'{zen_of_python_str.replace("i", "&")}')
