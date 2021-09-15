def filter_words(st):
    st = st[:0] + st[0].upper() + st[1:]
    for i in range(1, len(st)):
        st = st[:i] + st[i].lower() + st[i+1:]
    return st
