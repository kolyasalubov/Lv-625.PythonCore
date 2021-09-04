def create_array(n):
    res=[]
    for i in range(1,n+1): res+=[i]
    return res

print(create_array(7))

def create_array2(n):
    res=[]
    i=1
    while i<=n:
        res+=[i]
        i+=1
    return res

print(create_array2(4))
