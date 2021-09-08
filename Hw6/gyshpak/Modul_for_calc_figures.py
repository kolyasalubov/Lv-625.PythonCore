def square_rectangle(n1 : int, n2 : int) -> int:
    """
    calculates the square of ​​a rectangle
    """
    return(int(n1 * n2))
# def square_triangle(n1 : int, n2 : int, n3 : int):
def square_triangle(n123 : list) -> float:
    """
    calculates the square of ​​a triangle
    """
    n1 = n123[0]
    n2 = n123[1]
    n3 = n123[2]
    p = (n1 + n2 + n3)/2
    return(float(p * (p - n1) * (p - n2) * (p - n3)) ** 0.5)
def square_circle(radius : int) -> float:
    """
    calculates the square of ​​a circle 
    """
    return(3.1416 * radius ** 2)

if __name__ == '__main__':
    print("This modul for calculat square of figures")