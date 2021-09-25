
odd=[]
even=[]
not_div=[]

for i in range(1,11):
    if i%2==0:
       even.append(i)
    if i%3==0:
        odd.append(i)
    if i%3!=0 and i%2!=0:
        not_div.append(i)



print(f"Numbers, div by 3 in range {odd}")
print(f"Even numbers in range {even}")
print(f"Numbers, witch not div 2 and 3 in range {not_div}")