num_1 = float(input("Enter first object "))
num_2 = float(input("Enter second object "))
num_3 = float(input("Enter first object "))
num_4 = float(input("Enter second object "))

def distance(par1_2, par1_1, par2_1, par2_2):
    return round(((par1_1-par1_2)**2+(par2_1-par2_2)**2)**0.5,2)
work=distance(num_2,num_1,num_3,num_4)
print(f"Distance between two pairs is {work}")
