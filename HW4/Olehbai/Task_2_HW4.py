str_list = ['1', '6', '37', '5', '96', '11']

for n in str_list:
    print(f"Type of data is - {type(n)}")


a = 0
for n in str_list:
    str_list[a] = float(n)
    a += 1

for n in str_list:
    print(f"Type of data is - {type(n)}")
