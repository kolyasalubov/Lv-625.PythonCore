def space(cap, on, wait):
    """
    Function will return the number
    of passengers who didn’t fit in
    the bus or 0 if everyone fits
    """
    if cap - on <= wait:
        return abs(wait - (cap - on))
    else:
        return 0
