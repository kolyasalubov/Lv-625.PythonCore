import math


def rectangle(a,b):
    return(int(a)*int(b))

def triangle(a,b,c):
    p=(a+b+c)/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    return(s)

def circle(r):
    return(2*math.pi*r)

choise=input("Whitch object would you like to calculate?:")
if choise=="rectangle":
    a=int(input("Input length side 'a' "))
    b=int(input("Input length side 'b' "))
    print(f"Square of rectangle is:{round(rectangle(a,b),2)}")
elif choise=="triangle":
    a=int(input("Input length side 'a' "))
    b=int(input("Input length side 'b' "))
    c=int(input("Input length side 'c' "))
    print(f"Square of triangle is: {round(triangle(a,b,c),2)}")
elif choise=="circle":
    r=int(input("Input radius of circle "))
    print(f"Square of circle is: {round((circle(r)),2)}")

# a=int(input("Input length side 'a' "))
# b=int(input("Input length side 'b' "))
# c=int(input("Input length side 'c' "))      
# d=triangle(a,b,c)
# print(d)
