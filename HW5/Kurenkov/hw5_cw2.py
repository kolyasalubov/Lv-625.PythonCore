#If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.

def enough(cap, on, wait):
    if cap < (wait + on):
        return abs(cap - (wait + on))
    else:
        return 0

