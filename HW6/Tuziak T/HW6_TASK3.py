def count_str (a):

    cs = len(a)
    return cs

a = count_str("Softserv")
print(a)


def count_str_dic (string):

    l = [i for i in string]
    d = dict()
    for i in l:
        num = string.count(i)
        du = {i:num}
        d.update(du)
    return d

print(count_str_dic("Soft"))
print(count_str_dic("Softserv"))