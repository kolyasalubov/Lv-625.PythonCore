##### https://www.codewars.com/kata/grasshopper-summation/train/python
"""
Write a program that finds the summation of every number from 1 to num. 
The number will always be a positive integer greater than 0.

For example:
summation(2) -> 3
1 + 2

summation(8) -> 36
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
"""

def summation(num):
    import math
    my_list = list(range(1,num+1))
    return round(math.fsum(my_list))

# def summation(num):
#     return sum(range(num + 1))


print(summation(1))     # 1
print(summation(8))     # 36
print(summation(22))    # 253
print(summation(100))   # 5050
print(summation(213))   # 22791
