from math import pi, pow

def s_rectangle(a,b):
    return round(a*b, 2)

def s_triangle(a,h):
    s_triangle = 0.5*h*a
    return round(s_triangle, 2)

def s_circle(r):
    s_circle = pi*(pow(r,2))
    return round(s_circle, 2)