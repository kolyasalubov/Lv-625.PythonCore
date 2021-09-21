fib1 = fib2 = 1
 
n = input("Type N: ")
n=int(n)
if n==1: print(fib1)
else:
    if n<2: print(fib1,fib2,end=" ") # end=" " что б дальше писало в эту же строку
    else:
        n = int(n) - 2
        print(fib1,fib2,end=" ")
 
        while n > 0:
            fib1, fib2 = fib2, fib1 + fib2
            n -= 1
            print(fib2,end=" ")
 