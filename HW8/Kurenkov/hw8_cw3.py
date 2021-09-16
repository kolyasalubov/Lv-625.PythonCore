# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

def double_char(s):
    string = ''
    for i in s:
        string += i+i
    return string



