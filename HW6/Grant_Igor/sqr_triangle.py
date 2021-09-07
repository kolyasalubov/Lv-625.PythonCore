import math
def triangle(a, b, c):
    # Function will calculate the squere of the triangle
    p = (a+b+c)/2
    s_t = round(math.sqrt(p*(p-a)*(p-b)*(p-c)), 2)
    return s_t
