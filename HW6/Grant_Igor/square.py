import math
def triangle(a, b, c):
    # Function will calculate the square of the triangle
    p = (a+b+c)/2
    s_t = round(math.sqrt(p*(p-a)*(p-b)*(p-c)), 2)
    return s_t

def rectangle(a, b):
    # Function will calculate the square of the rectangle
    s_r = round((a*b), 2)
    return s_r

def circle(r):
    # Function will calculate the square of the circle
    s_c = round(math.pi*(r**2), 2)
    return s_c