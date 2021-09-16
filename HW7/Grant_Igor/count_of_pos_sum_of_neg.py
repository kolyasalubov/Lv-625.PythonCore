"""
Function returns the number of positive numbers in the list
and sum of all negative numbers
If list is empty or equal to zero - returns empty list
"""
def function(list):
    if len(list) == 0:
        return []
    num_of_pos = 0
    sum_of_neg = 0
    for i in list:
        if i > 0:
            num_of_pos += 1
        if i < 0:
            sum_of_neg += i
    return [num_of_pos, sum_of_neg]

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
print(function(list))
