##### https://www.codewars.com/kata/double-char/train/python
"""
Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
double_char("String") ==> "SSttrriinngg"
double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"
double_char("1234!_ ") ==> "11223344!!__  "
"""

def double_char(s):
    ss = []
    for i in range(0,len(s)):
        ss.append(s[i])
        ss.append(s[i])
    return "".join(ss)
    
string1 = "String"
print(double_char(string1))     # SSttrriinngg

string2 = "Hello World"
print(double_char(string2))     # HHeelllloo  WWoorrlldd

string3 = "1234!_ "
print(double_char(string3))     # 11223344!!__  

