our_list = [35,57,81,93,]

for i in our_list:
    print(f"Type of data befor change is {type(i)}")

n = 0
for i in our_list:
    our_list[n] = float(i)
    n += 1

for i in our_list:
    print(f"Type of data after change is {type(i)}")
