def return_max_number(*args):
    """" 
    returning the largest 
    number of two numbers
    """
    return max(*args)
num1, num2 = int(input()), int(input())
print("The largest number is:", return_max_number(num1,num2))
