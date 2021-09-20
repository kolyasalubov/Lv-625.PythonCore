def num_characters(string):
    return {character: string.count(character) for character in string}

new_string = input("Enter string: ")

characters = num_characters(new_string)
print(characters)