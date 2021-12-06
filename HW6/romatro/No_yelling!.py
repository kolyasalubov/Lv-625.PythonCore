def filter_words(st):
    st_new_1=st[1:].lower()
    st_new_2=st[0].title()
    st_new_join=st_new_2+st_new_1
    st_new_final=' '.join(st_new_join.split())
    return st_new_final