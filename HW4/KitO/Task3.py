##### Home_Work4_Task_3 ("Loops" Slide 15)
"""
Print Fibonacci numbers up to the entered number n, using cycles. 
Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.
"""
        
def fib_while(n):
    """
    This function returns the Fibonacci numbers up to the entered number n
    """
    if n == 0:
        f = []
    elif n == 1:
        f = [0]
    else:
        f = [0, 1]
        i = 2
        while i < n:
            f.append(f[i-2]+f[i-1])
            # f.insert(i, (f[i-2]+f[i-1]))      #### Так не працює: f = f.insert(i, (f[i-2]+f[i-1]))
            i += 1
    return f

print(fib_while(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def fib_for(n):
    """
    This function returns the Fibonacci numbers up to the entered number n
    """
    if n == 0:
        f = []
    elif n == 1:
        f = [0]
    else:
        f = [0, 1]
        for i in range(2, n):
            f.append(f[i-2] + f[i-1])
    return f

print(fib_for(8))   # [0, 1, 1, 2, 3]

def fib_number(m):
    """
    This function returns the last Fibonacci number in the range according the entered number n
    """
    return fib_for(m)[-1]

print(fib_number(8))    # 13
