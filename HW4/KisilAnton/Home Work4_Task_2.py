list=[int(i) for i in input('Enter the list: ')]
print('List that contains elements of integer type: ',list)
for i in range(len(list)):
    list[i]=float(list[i])
print('Change the type of these elements to a floating type: ',list)