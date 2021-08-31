value=input('Enter the four-digit value: ')
print('{}*{}*{}*{} ='.format(value[0],value[1],value[2],value[3]), int(value[0])*int(value[1])*int(value[2])*int(value[3]))
print('In reverse order:', value[::-1])
print('Sorted:', ''.join(sorted(value)))