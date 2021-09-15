def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return[]
    sum1 = 0
    sum2 = 0
    for i in arr:
        if i > 0:
            sum1 += 1
        else:
            sum2 += i
    return [sum1,sum2]

my_list = [1,2,3,4,5,6,7,8,9,10,-11,-12,-13,-14,-15]
print(count_positives_sum_negatives(my_list))