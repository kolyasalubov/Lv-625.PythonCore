import math

import square


choise=input("Whitch object would you like to calculate?:")
if choise=="rectangle":
    a=int(input("Input length side 'a' "))
    b=int(input("Input length side 'b' "))
    print(f"Square of rectangle is:{round(square.rectangle(a,b),2)}")
elif choise=="triangle":
    a=int(input("Input length side 'a' "))
    b=int(input("Input length side 'b' "))
    c=int(input("Input length side 'c' "))
    print(f"Square of triangle is: {round(square.triangle(a,b,c),2)}")
elif choise=="circle":
    r=int(input("Input radius of circle "))
    print(f"Square of circle is: {round((square.circle(r)),2)}")
