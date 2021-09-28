a = 0
b = 1
n = int(input("please input number to calculate fibo:"))
list = [0,1]
for arg in range(n-1):
    c = a + b
    a = b
    b = c
    list.append(c)

print(list)