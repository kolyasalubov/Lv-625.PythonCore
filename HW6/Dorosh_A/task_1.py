def largest_number (a, b):
    '''Functoion return the largest number
    of two numbers
    '''
    return  f"The largest number is {max(a, b)}"

num1 = int(input("Enter number "))
num2 = int(input("Enter number "))
work = largest_number(num1, num2)
print (work)
