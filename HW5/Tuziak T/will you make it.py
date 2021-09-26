distance_to_pump = int(input("Введіть дистанцію до насосу"))
average = 25
fuel_left = 2
def zero_fuel(distance_to_pump, average, fuel_left):
    if distance_to_pump/average <= fuel_left:
        return True
    else:
        return False
work = zero_fuel(distance_to_pump, average, fuel_left)
print(work)