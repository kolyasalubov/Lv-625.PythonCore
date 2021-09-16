##### Home_Work5_Task_1 ("Collection" Slide 39)
"""
In the range from 1 to 10 determine 
even numbers that are divisible by 2,
odd numbers, which are divisible by 3,
numbers that are not divisible by 2 and 3.
"""

n = int(input("Enter your number for range: "))
L = list(range(1,n+1))
print(L)
even = []               # парні числа
odd = []                # непарні числа, що діляться на 3
not_div_by_2_3 = []     # прості числа
other = []
for i in range(0,n-1):
    if L[i]%2 == 0:
        even.append(L[i])
    elif L[i]%3 == 0:
        odd.append(L[i])
    elif L[i]%2 != 0 and L[i]%3 != 0:
        not_div_by_2_3.append(L[i])
    else:
        other.append(L[i])
print(even)
print(odd)
print(not_div_by_2_3)
print(other)
         



