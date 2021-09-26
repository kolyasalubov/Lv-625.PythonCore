def count_sheeps(sheep: list) -> int:
    sheeps = sheep.count(True)
    return sheeps


print(count_sheeps(
    [True,  True,  True,  False,
    True,  True,  True,  True ,
    True,  False, True,  False,
    True,  False, 0, True ,
    True,  True,  True,  True ,
    False, False, True,  True]))