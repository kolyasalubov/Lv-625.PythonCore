f1 = f2 = 1
 
n = int(input("Input number of Fibonaci"))
 
print(f1, f2)
i = 2
while i < n:
    sumf = f1 + f2
    f1 = f2
    f2 = sumf
    print(sumf)
    i +=1



