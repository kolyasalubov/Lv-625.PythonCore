number = input("Enter your number: ")
number = str(number)
print("Reversed number is : ", number[::-1])
sum = 0
for n in number:
    sum += int(n)
print("Sum of all numbers is: ", sum)
list = [i for i in number]
sorted_list = sorted(list)
print("Your sorted list is: ", sorted_list)
