str_list = ['1', '6', '37', '5', '96', '11']

for n in str_list:
    print(f"Type of data is - {type(n)}")
print(str_list, '\n')

a = 0
for n in str_list:
    str_list[a] = float(n)
    a += 1
print(str_list)

for n in str_list:
    print(f"Type of data is - {type(n)}")
