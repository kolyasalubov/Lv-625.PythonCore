##### https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python
"""
Given an array of integers.
Return an array, where the first element is the count of positives numbers 
and the second element is sum of negative numbers.
If the input array is empty or null, return an empty array.
Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
"""

def count_positives_sum_negatives(arr):
    if len(arr) == 0 :
        return arr
    else : 
        import math
        positives = []
        negatives = []
        for i in range(0, len(arr)):
            if arr[i] > 0 :
                positives.append(arr[i])
            elif arr[i] <= 0 :
                negatives.append(arr[i])
        return [len(positives), round(math.fsum(negatives))]

array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
print(count_positives_sum_negatives(array1))    # [10, -65]

array2 = [0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]
print(count_positives_sum_negatives(array2))    # [8,-50]

array3 = [1]
print(count_positives_sum_negatives(array3))    # [1,0]

array4 = [-1]
print(count_positives_sum_negatives(array4))    # [0,-1]

array5 = [0,0,0,0,0,0,0,0,0]
print(count_positives_sum_negatives(array5))    # [0,0]

array6 = []
print(count_positives_sum_negatives(array6))    # []
