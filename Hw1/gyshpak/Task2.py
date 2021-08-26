a = int(input("Input a "))
b = int(input("Input b "))

print("%d + %d = %d" %(a, b, a + b))
print("%s - %s = %s" %(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{1} / {2} = {0}".format(a / b, a, b))
print("{x} ** {y} = {z}".format(x = a, y = b, z = a**b))