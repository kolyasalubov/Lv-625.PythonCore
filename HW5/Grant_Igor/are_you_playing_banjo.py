def banjo(name):
    """
    Function shows whether you play banjo
    parameter name must be string
    """
    if name[0] == "R" or name[0] == "r":
        return name + ", you play banjo"
    else:
        return name + ", you don’t play banjo"
