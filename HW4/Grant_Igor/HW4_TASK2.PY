number = input("Number: ")
number = str(number)
list_number = list(number)
for i in range(len(list_number)):
    list_number[i] = float(list_number[i])
print(list_number)
