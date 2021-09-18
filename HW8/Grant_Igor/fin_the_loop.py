def list_animals(animals):
    list = ''
    for i in range(animals):
        list += str(i + 1) + '. ' + animals[i] + '\n'
    return list
print(list_animals(['cat', 'dog', 'elephant']))