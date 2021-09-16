##### Home_Work4_Task_2 ("Loops "Slide 14)
# Create a list that contains elements of integer type, 
# then use the loop to change the type of these elements to a floating type.

customer_number = int(input("Enter your number under 100: "))
list_int = list(range(0,customer_number,1))
n = 0
for n in list_int:
    list_int[n] = float(list_int[n])
    n += 1
print(list_int)
