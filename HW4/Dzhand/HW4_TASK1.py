number = int(input("Input number: "))

factor = 1

for i in range (1, number+1):
    factor *= i
    print (format(number), factor)
