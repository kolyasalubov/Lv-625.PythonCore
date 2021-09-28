def enough(cap, on, wait):
    if cap < on or (cap-on-wait)>=0:
        return 0
    else:
        return abs(wait-(cap-on))