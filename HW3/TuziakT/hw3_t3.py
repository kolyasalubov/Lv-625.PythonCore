"""
Swap the values ​​of two variables- 
without using the third variable.
"""
a = 5           # 101
b = 6           # 110

a = a ^ b     # 11       
b = a ^ b    # 5
a = a ^ b    # 6

print (a)
print (b)
"""
this metod is fun cause we are savin 1 extra bit by using XOR
what it basically do?
compares two binary numbers bitwise. If both bits are the same, XOR outputs 0.
If the bits are different, XOR outputs 1.
Якщо ультра по поростому і як то кажуть in General.
ми не тратимо екстра пам'яті але всерівно можемо побачити наш Autput
"""