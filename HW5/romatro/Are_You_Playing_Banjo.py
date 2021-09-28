def are_you_playing_banjo(name):
    for letter in name:
        if letter[0] in ("R", "r"):
            return name + " plays banjo"
        else:
            return name + " does not play banjo"