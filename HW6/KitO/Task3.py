##### Home_Work6_Task_3 ("Function" Slide 39)
"""
Write a function that calculates the number of characters 
included in a given string.
"""

def count_str (a):
    """
    Функція обчислює кількість символів, включених до даного рядка.
    """
    cs = len(a)
    return cs

a = count_str("Hello world")
print(a)


def count_str_dic (string):
    """
    input: "hello"
    output: {"h":1, "e":1, "l":2, "o":1}
    """
    dic = dict(string.split())
    return dic

print(count_str_dic("Hello world"))

