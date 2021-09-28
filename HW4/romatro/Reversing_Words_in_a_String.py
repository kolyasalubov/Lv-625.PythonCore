def reverse(st):
    st = st.split()
    st_new = st[::-1]
    st = tuple(st_new)
    st = str(' '.join(st))
    return st