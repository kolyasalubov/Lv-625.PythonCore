_list = "Hello world"
def functoin1(smth):
    rev_list = smth.split()[::-1]
    return ' '.join([str(i) for i in rev_list])
work = functoin1(_list)
print(work)
