name = input("Enter your name: ")
def player_banjo(name):
    if name[0]=="r" or name[0]=="R":
        return (f"{name} plays banjo")
    else:
        return (f"{name} does not play banjo")
work = player_banjo(name)
print(work)
