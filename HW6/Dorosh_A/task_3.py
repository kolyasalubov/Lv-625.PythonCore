
num_of_characters = input("Enter your sentence ")
def func_calculate(num_of_characters):
    return num_of_characters.count("", 0, -1)
work=func_calculate(num_of_characters)
print(f"Number of characters in string is {work}")
