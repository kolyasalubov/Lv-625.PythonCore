The_Zen_of_Python='Beautiful is better than ugly. \
Explicit is better than implicit. \
Simple is better than complex. \
Complex is better than complicated. \
Flat is better than nested. \
Sparse is better than dense. \
Readability counts. \
Special cases aren\'t special enough to break the rules. \
Although practicality beats purity. \
Errors should never pass silently. \
Unless explicitly silenced. \
In the face of ambiguity, refuse the temptation to guess. \
There should be one-- and preferably only one --obvious way to do it. \
Although that way may not be obvious at first unless you\'re Dutch. \
Now is better than never. \
Although never is often better than *right* now. \
If the implementation is hard to explain, it\'s a bad idea. \
If the implementation is easy to explain, it may be a good idea. \
Namespaces are one honking great idea -- let\'s do more of those!'
print('Task 1:\n')
start=0
i=0
while The_Zen_of_Python.find('better',start)!=-1:
    start=1+The_Zen_of_Python.find('better',start)
    i+=1
print("\"better\" is included in the list %d times" % i)
start=0
i=0
while The_Zen_of_Python.find('never',start)!=-1:
    start=1+The_Zen_of_Python.find('never',start)
    i+=1
print("\"never\" is included in the list %d times" % i)
while The_Zen_of_Python.find('is',start)!=-1:
    start=1+The_Zen_of_Python.find('is',start)
    i+=1
print("\"is\" is included in the list %d times" % i)
print('\n Task 2: \n \n',The_Zen_of_Python.upper(),)
print('\n Task 3: \n \n',The_Zen_of_Python.replace('i','&'))