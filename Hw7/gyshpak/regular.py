import re
def check_pass(in_pass):
    count_check = 0
    my_answer = "You password must contain"
    if re.fullmatch(r'[a-zA-Z0-9$#@]{6,16}', in_pass):
        count_check += 1
        print('1')
    else:
        my_answer += " from 6 to 16 simbols "
    if re.fullmatch(r'.*[a-z]+.*', in_pass):
        count_check += 1
        print('2')
    else:
        my_answer += ", one or more a-z simbols "
    if re.fullmatch(r'.*[A-Z]+.*', in_pass):
        count_check += 1
        print('3')
    else:
        my_answer += ", one or more A-Z simbols "
    if re.fullmatch(r'.*[0-9]+.*', in_pass):
        count_check += 1
        print('4')
    else:
        my_answer += ", one or more 0-9 simbols "
    if re.fullmatch(r'.*[$#@]+.*', in_pass):
        count_check += 1
        print('5')
    else:
        my_answer += ", one or more @#$ simbols "
    
    return ("Your password is correct" if count_check == 5 else my_answer)
    
print(check_pass(input('insert password ')))