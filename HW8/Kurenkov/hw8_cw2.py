# Your collegue wrote an simple loop to list his favourite animals. But there seems to be a minor mistake in the grammar, which prevents the program to work. Fix it! :)
# If you pass the list of your favourite animals to the function, you should get the list of the animals with orderings and newlines added.


def list_animals(animals):
    ord_list = ''
    for i in range(len(animals)):
        ord_list += str(i + 1) + '. ' + animals[i] + '\n'
    return ord_list




