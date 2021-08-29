def reverse(st):
    # Your Code Here
    my_list = []
    my_str = ""
    for i in st:
         if i == " " and my_str != "":
            my_list.append(my_str)
            my_str = ""
         elif i != " ":
            my_str += i
    if my_str != "":
        my_list.append(my_str)
    my_list.reverse()
    st = " ".join(my_list)
    return st