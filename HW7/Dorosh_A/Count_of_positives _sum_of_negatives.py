array = [1,4,2,4,-3,-6,-6,-87]

def functoin1(smth):
    count_pos_number = 0
    sum_neg_num = 0
    if smth == [] or sum(smth)==0:
        smth = []
        return (smth)
    else:
        for num in smth:
            if num >=1:
                count_pos_number += 1
        for num2 in smth:
            if num2 <0:
                sum_neg_num =  sum_neg_num+num2
        smth=[count_pos_number, sum_neg_num]
        return (smth)
work = functoin1(array)
print(work)
