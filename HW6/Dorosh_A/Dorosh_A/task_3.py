
num_of_characters = input("Enter your sentence ")
def func_calculate(num_of_characters):
    return num_of_characters.count("", 0, -1)
work=func_calculate(num_of_characters)
print(f"Number of characters in string is {work}")

#####variant_2
def calculate(str1):
    """Write a function that calculates the number of characters included in a given string"""
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(calculate(input("Enter ")))
