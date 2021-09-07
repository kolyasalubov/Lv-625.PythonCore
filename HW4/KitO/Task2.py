##### Home_Work4_Task_2 ("Loops "Slide 14)
# Create a list that contains elements of integer type, 
# then use the loop to change the type of these elements to a floating type.

customer_number = int(input('Enter your number: '))
print(f'Your number is: {customer_number}')
list_int = list(range(0,customer_number,2))
print(list_int)

n = 0
for n in list_int:
    list_float[n] = float(list_int[n])
    n += 1
print(list_float)
