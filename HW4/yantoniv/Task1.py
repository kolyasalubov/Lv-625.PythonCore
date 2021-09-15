number = int(input('Enter number: '))

def factorial_number(num):
    fact_num = 1
    for i in range(1, num+1):
        fact_num *= i
    return fact_num

print(factorial_number(number))
