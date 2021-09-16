def reverse(str_r):
    str_r=str_r[::-1]
    return str_r



def reverse_words(str_r):
    n=len(str_r)
    if(n==1):
        return str_r
    str2=str_r.split("")
    size=len(str2)
    rev_all=""
    for i in range(size):
        rev=reverse(str2[i])
        rev_all=rev_all+rev+" "
        print(reverse(rev_all)) #dont understand why its not working and it gives me "TKEFREP SI YMEDACA EVRESTFOS"


str_r="TKEFREP SI YMEDACA EVRESTFOS"
print(reverse(str_r))