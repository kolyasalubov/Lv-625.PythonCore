number = int(input('Enter number: '))

def fibonacci (n):
    if n<= 0:
       return "Incorrect Output"
    data = [0, 1]
    if n > 2:
        for i in range (2, n+1):
            data.append(data[i-1] + data[i-2])
    return data[n]
 
print(fibonacci(number))