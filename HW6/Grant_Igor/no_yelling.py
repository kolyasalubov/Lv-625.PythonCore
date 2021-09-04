def converter(sentence):
    """
    Function converts all symbols of the string
    into lower case and capitalizes the beginning
    of the sentence
    """
    if sentence.upper() or sentence.lower():
        return sentence.capitalize()
