import sys

print('Insert a')
a = int(sys.stdin.readline())

print('Insert b')
b = int(sys.stdin.readline())

if a > b:
    print (f"{a} > {b}")
elif a < b:
    print ("a < b")
else: 
    print("a = b")
