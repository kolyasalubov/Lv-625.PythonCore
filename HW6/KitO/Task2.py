##### Home_Work6_Task_2 ("Function" Slide 38)
"""
Write a program that calculates the square of ​​a rectangle, triangle and circle 
(write three functions to calculate the square, 
and call them in the main program depending on the user's choice).
"""

def sqRectangle(a: int, b: int) -> int:
    """
    Функція розраховує площу прямокутника.
    """
    squareR = a * b
    return squareR

print(sqRectangle(5,6))

def SqTriangle(a: int, b: int, c: int) -> int:
    """
    Функція розраховує площу трикутника за формулою Герона,
    якщо відома довжина трьох сторін трикутника.
    """
    p = (a + b + c) / 2
    squareT = (p * (p - a) * (p - b) * (p - c)) ** (1/2)
    return squareT

print(SqTriangle(5,6,8))

def sqTriangle(a: int, b: int) -> int:
    """
    Функція розраховує площу прямокутного трикутника за формулою Герона,
    якщо відома довжина двох катетів цього трикутника.
    """
    c = (a ** 2 + b ** 2) ** (1/2)
    p = (a + b + c) / 2
    squareT = (p * (p - a) * (p - b) * (p - c)) ** (1/2)
    return squareT

print(sqTriangle(5,6))

def sqCircle(r: int) -> int:
    """"""
    pi = 3.1415926535
    squareC = pi * r ** 2
    return squareC

print(sqCircle(3))
