# Given an array of integers.
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.
# If the input array is empty or null, return an empty array.
# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

def count_positives_sum_negatives(arr):
    if not arr:
        return []
    counts = [0, 0]
    for i in arr:
        if i > 0:
            counts[0] += 1
        else:
            counts[1] += i

    return counts




