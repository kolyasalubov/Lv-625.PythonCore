##### https://www.codewars.com/kata/53da6d8d112bd1a0dc00008b/train/python
"""
In this kata you will create a function that takes in a list 
and returns a list with the reverse order.
"""

def reverse_list(l):
    r = l.reverse()
    return l

list1 = [1,2,3,4]
list2 = [3,1,5,4]

print(reverse_list(list1))  # [4, 3, 2, 1]
print(reverse_list(list2))  # [4, 5, 1, 3]
