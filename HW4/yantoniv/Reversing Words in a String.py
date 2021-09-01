text = input()

def reversing_text(text):
    words = text.split(' ')
    string =[]
    for word in words:
        string.insert(0, word)
 
    return " ".join(string)

print(reversing_text(text))