def count_positives_sum_negatives(list):
    positive_num_counter = 0
    sum_of_negative_num = 0
    if list == [0] or list == []:
        return []
    else:
        for num in list:
            if num > 0:
                positive_num_counter += 1
            else:
                sum_of_negative_num += num
    return [positive_num_counter, sum_of_negative_num]
