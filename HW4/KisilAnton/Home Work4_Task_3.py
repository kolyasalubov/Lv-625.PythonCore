n=int(input('Enter the n for Fibonacci numbers: '))
Fibonacci=[]
if n>=0:
    Fibonacci.append(0)
if n>=1:
    Fibonacci.append(1)
if n>1:
    a1=0
    a2=1
    for i in range(1,n):
        a=a1+a2
        Fibonacci.append(a)
        a1=a2
        a2=a
print('Fibonacci numbers: ',Fibonacci)
