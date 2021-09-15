word = input()
word_list = list(word)
num_of_the_letters = {}
for letter in word_list:
    if letter not in num_of_the_letters:
        num_of_the_letters[letter] = 1
    else:
        num_of_the_letters[letter] += 1
print(num_of_the_letters)
