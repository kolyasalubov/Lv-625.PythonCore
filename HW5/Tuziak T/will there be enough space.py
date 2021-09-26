def enough(cap,on,wait):
    if cap < (wait + on):
        return abs(cap - (wait + on))
    else:
        return 0