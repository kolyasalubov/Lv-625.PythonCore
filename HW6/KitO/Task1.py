##### Home_Work6_Task_1 ("Function" Slide 31)
"""
Write a function that returns the largest number of two numbers 
(use DocStrings documentation strings in the function). 
"""

def max(num1, num2):
    """
    This function returns the largest number of two numbers.
    """
    if num1 > num2:
        return num1
    else:
        return num2

a = max(5, 8)
b = max(5, 0)
c = max(-1, -3)
d = max(-5, 0)
print(a, b, c, d)


