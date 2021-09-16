# Write a function that calculates the number of characters included in a given string

def char_count(string):
    counts = {}
    for char in string:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    return counts




