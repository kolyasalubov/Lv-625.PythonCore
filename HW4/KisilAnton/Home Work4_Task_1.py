number=int(input('Enter number: '))
factorial=1
for i in range(number):
    factorial=factorial*(i+1)
print('%d!=%d'%(number,factorial))
