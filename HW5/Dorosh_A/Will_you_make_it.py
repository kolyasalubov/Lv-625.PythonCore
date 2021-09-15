distance_to_pump = int(input("Enter distace to pump"))
average = 25
fuel_left = 2
def zero_fuel(distance_to_pump, average, fuel_left):
    if distance_to_pump/average <= fuel_left:
        return True
    else:
        return False
work = zero_fuel(distance_to_pump, average, fuel_left)
print(work)
