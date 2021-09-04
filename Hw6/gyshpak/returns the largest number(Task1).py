def returns_the_largest_number(arg1 : int, arg2 : int):
    """
    This funktion returned maximum of thwo entered numbers
    """
    return(max(arg1,arg2))

n1 = input("enter first number ")
n2 = input("enter theckond number ")
print(f"maimum of {n1} and {n2} is", returns_the_largest_number(n1,n2))
