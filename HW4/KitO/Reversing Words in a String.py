###### https://www.codewars.com/kata/57a55c8b72292d057b000594/train/python
"""
You need to write a function that reverses the words in a given string. 
A word can also fit an empty string. 
If this is not clear enough, here are some examples:
As the input may have trailing spaces, 
you will also need to ignore unneccesary whitespace.
Example (Input --> Output)
"Hello World" --> "World Hello"
"Hi There." --> "There. Hi"
"""

# def reverse(st):
#     # Your Code Here
#     return st

def reverse(st):
    s = list(st.split())
    # rev_list = reverse(s)
    # rev_str = ''.join(reverse(list(st.split())))
    return s

a = reverse("Hello World")
print(a)


