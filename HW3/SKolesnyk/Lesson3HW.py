
#Task1
import this 
import codecs
ss = codecs.encode(this.s, 'rot13')
better_word = "better"
never_word = "never"
is_word = " is "

count_better = ss.count(better_word)
print("BETTER occurs {i} times".format(i=count_better))

count_never = ss.count(never_word)
print("NEVER occurs {i} times".format(i=count_never))

count_is = ss.count(is_word)
print("IS occurs {i} times".format(i=count_is))

ss_upper = ss.upper()
print(ss_upper)

ss_replaced = ss.replace("i", "&")
print(ss_replaced)

#Task2
number = 3751
sorted_list = sorted(str(number))
s = ""
sorted_num = s.join(sorted_list)
print("sorted number = ", sorted_num)

reversed_list = str(number)[::-1]
print("reversed number = ", reversed_list)
sum = 0
for n in reversed_list:
    sum+=int(n)
print("summa = ", sum)

#Task3
a = 3
b = 2
a = a+b
b= a-b
a = a - b
print("a = ",a)
print("b = ", b)