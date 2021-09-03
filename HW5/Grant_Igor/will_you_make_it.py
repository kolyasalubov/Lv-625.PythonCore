def car_range(range, mpg, fuel):
    # Fucntion returns True or False
    if range < 0 or mpg < 0 or fuel < 0:
        return "Input values must be positive!"
    else:
        return bool(range / mpg <= fuel)
