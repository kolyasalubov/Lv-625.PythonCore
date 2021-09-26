def count_positives_sum_negatives(arr):
    if len (arr) == 0:
        return []
        sum_of_neg = 0
        sum_of_pos = 0
        for i in arr:
            if i > 0:
                sum_of_pos =+ 1
            elif i < 0:
                sum_of_neg += i
        return [sum_of_pos, sum_of_neg]
