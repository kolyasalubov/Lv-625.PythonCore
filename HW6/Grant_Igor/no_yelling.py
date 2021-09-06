def converter(sentence):
    """
    Function converts all symbols of the string
    into lower case and capitalizes the beginning
    of the sentence
    """
    sentence = ' '.join(sentence.split())
    return sentence.capitalize()
