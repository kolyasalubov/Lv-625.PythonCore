def filter_words(st):
    st = ' '.join(st.split())
    return st[0].upper() + st.lower()[1:]

print(filter_words("hello     WORLDS"))

def filter_words_2(st):
    return((' '.join(st.split())).capitalize())

print(filter_words_2("   hello     WORLDS"))
