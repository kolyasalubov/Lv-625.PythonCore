def numb_characters_on_str(arg : str) -> tuple:
    """
    returned calculate the number of characters included in a given string 
    """
    return(len(arg),{x1:arg.count(x1) for x1 in arg})

our_len = numb_characters_on_str(input("enter string "))
print("in your string is {} characters:\n{}".format(our_len[0],our_len[1]))
