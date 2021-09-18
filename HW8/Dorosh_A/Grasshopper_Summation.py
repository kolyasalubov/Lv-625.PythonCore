def summation(num):
    sum_all = 0
    if num <=0:
        return ("Number must be positive and not equal 0")
    else:
        for sum in range(1, num+1):
            sum_all = sum_all+sum 
    return f"The summation of every number from 1 to {num} is {sum_all}"
