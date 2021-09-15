def enough(cap, on, wait):
    # Your code here
    hawe = cap-on
    if wait >= hawe:
        return wait-hawe
    else:
        return 0
