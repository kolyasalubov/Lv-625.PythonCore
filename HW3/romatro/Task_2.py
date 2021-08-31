x = int(input("please enter the number to process: "))
x1 = str(x)
x2 = list(x1)
print(int(x2[0])*int(x2[1])*int(x2[2])*int(x2[3]))
x3 = x2[::-1]
print(x3)
x4 = [int(i) for i in x1]
print(sorted(x4))