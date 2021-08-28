#Task1
def factorial(n):
    f=1
    i=1
    while i<=n:
        f=f*i
        i+=1
    return f

#print(factorial(8))

#Task2
l = [1,3,2,4,5,8]
#print(type(l[0]))
for i in range(len(l)-1):
    l[i]=float(l[i])
#print(type(l[1]))

#Task3
n=13
i=1
j=0
sum=0
fib=[0,1]
while i <=n:
    sum = fib[i]+fib[j]
    fib.append(sum)
    j=i
    i+=1
#print(fib)