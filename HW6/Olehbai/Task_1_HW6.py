def largest(arg_1, arg_2):
    """
    This function returns the largest number of two numbers.
    """
    if arg_1 > arg_2:
        return f"largest {arg_1}"
    else:
        return f"largest {arg_2}"
arg_1 = int(input("Enter first num: "))
arg_2 = int(input("Enter second num: "))
print(largest(arg_1, arg_2))