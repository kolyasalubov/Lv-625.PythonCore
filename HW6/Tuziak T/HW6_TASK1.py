def returns_the_largest_number(arg1 : int, arg2 : int):
    return(max(arg1,arg2))

n1 = input("Введіть перше число ")
n2 = input("Введіть друге число ")
print(f"maximum of {n1} and {n2} is", returns_the_largest_number(n1,n2))