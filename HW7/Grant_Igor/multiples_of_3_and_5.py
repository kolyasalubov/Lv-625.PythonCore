# Function will find the sum of all multiples of 3 and 5
# without repetition of the same number twice
def function(number):
    sum = 0
    for i in range(number):
        if i %3 == 0 or i %5 == 0:
            sum += i
    return [sum]
print(function(10))