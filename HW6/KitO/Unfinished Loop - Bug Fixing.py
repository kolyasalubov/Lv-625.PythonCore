##### https://www.codewars.com/kata/unfinished-loop-bug-fixing-number-1/train/python
"""
Oh no, Timmy's created an infinite loop! 
Help Timmy find and fix the bug in his unfinished for loop!
"""

def create_array(n):
    res=[]
    i=1
    while i <= n: 
        res += [i]
        i += 1
    return res

a = create_array(5)
print(a)
