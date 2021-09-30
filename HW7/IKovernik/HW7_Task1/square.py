import math


def rectangle(a,b):
    return(int(a)*int(b))

def triangle(a,b,c):
    p=(a+b+c)/2
    # s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    s=math.pow((p*(p-a)*(p-b)*(p-c)),0.5)

    return(s)

def circle(r):
    return(2*math.pi*r)