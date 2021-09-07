# Create a list that contains elements of integer type, then use the loop to change the type of these elements to a floating type.
# (Hint: use the built-in float () function).

list_of_integers = input("Input your number: ")
list_of_float = []
for i in list_of_integers:
    list_of_float.append(float(i))

print(list_of_float)
