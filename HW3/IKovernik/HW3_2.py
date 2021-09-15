argument=int(input("Input argument "))
sum=0
mult=1
sort = "".join(sorted(str(argument)))
while argument>0:
    digit = argument % 10
    sum = sum+digit
    mult = mult*digit
    argument = argument // 10
print(f"Sum of numbers = {sum}")
print(f"Product of numbers = {mult}")
print(f"Sorted argument is: {sort}")