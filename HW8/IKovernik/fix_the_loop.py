def double_char(s):
    dup = str()  # a new, empty string.
    for char in s:
       dup += char + char
       
    return dup

s = "abc jhL"
s=double_char(s)
print(s)