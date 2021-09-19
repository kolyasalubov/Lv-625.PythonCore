def summation(num):
    my_sum = 0
    for i in range(num+1):
        my_sum += i
    return my_sum

print(summation(int(input('enter number '))))