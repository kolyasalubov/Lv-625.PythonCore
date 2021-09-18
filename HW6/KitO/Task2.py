##### Home_Work6_Task_2 ("Function" Slide 38)
"""
Write a program that calculates the square of ​​a rectangle, triangle and circle 
(write three functions to calculate the square, 
and call them in the main program depending on the user's choice).
"""

def sqRectangle(a: int, b: int) -> int:
    """
    Функція розраховує площу прямокутника,
    якщо відома його довжина та ширина.
    """
    return a * b

print(sqRectangle(5,6))     # 30

def SqTriangle(a: int, b: int, c: int) -> int:
    """
    Функція розраховує площу трикутника за формулою Герона,
    якщо відома довжина трьох сторін трикутника.
    """
    p = (a + b + c) / 2
    squareT = (p * (p - a) * (p - b) * (p - c)) ** (1/2)
    return squareT

print(SqTriangle(5,6,8))    # 14.981238266578634

def sqTriangle(a: int, b: int) -> int:
    """
    Функція розраховує площу прямокутного трикутника за формулою Герона,
    якщо відома довжина двох катетів (a,b) цього трикутника.
    """
    return 0.5 * a * b

print(sqTriangle(5,6))      # 15.0

def sqCircle(r: int) -> int:
    """
    Функція розраховує площу кола, якщо відомо радіус (r).
    """
    pi = 3.1415926535
    return pi * (r ** 2)

print(sqCircle(3))      # 28.2743338815
