newlist_1=[]
newlist_2=[]
newlist_3=[]
for list_element in range(1,11):
    check = list_element % 2
    check_for_div_by_2 = list_element / 2
    if check==0 and check_for_div_by_2 >=1:
        newlist_1.append(list_element)
    elif check!=0:
        check_3 = list_element % 3
        check_for_div_by_3 = list_element / 3
        if check_3==0:
            newlist_2.append(list_element)
        else:
            newlist_3.append(list_element)
print("even numbers that are divisible by 2:",newlist_1)
print("odd numbers that are divisible by 3:",newlist_2)
print("numbers that are not divisible by 2 and 3", newlist_3)