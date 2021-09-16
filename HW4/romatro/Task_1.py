fact = int(input("please enter the value for factorial calculation: "))
if fact < 0:
    print("the value can't be calculated")
elif fact == 0:
    print("the value is 1")
else:
    a=list(range(1,fact+1))
    result = 1
    for x in a:
         result = result * x
    print ("the value is", result)