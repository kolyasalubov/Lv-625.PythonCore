number_1 = int(input("please ented number_1: "))
number_2 = int(input("please ented number_2: "))
def number_comparator (num_1=number_1,num_2=number_2):
    if num_1 > num_2:
        print (f"{num_1} is the largest number")
    elif num_1<num_2:
        print (f"{num_2} is the largest number")
    else: 
        print (f"{num_1} and {num_2} numbers are equal")

number_comparator()