for i in range(1,10):
    if i % 2 == 0 :
        print(i)

for i in range(1,10):
    if i % 2 == 0:
        continue
    print(i)

for i in range(1,10):
    if i % 2 != 0:
        print(i)

our_list = [2,4,6,8,1,18,26,34,68,2,7]
for i in our_list:
    if i % 2 != 0:
        break
    else:
        print(i)
