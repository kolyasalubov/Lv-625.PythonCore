
number = int(input("Enter "))
def function1(smth):
    list_num = []
    if smth <=0:
        return 0
    else:
        for i in range (0, smth):
            if i % 3 == 0 and i %5==0:       
                list_num.append(i)
            elif i % 3 == 0:
                list_num.append(i)
        print(list_num)
    return sum(list_num)

work = function1(number)
print(work)
