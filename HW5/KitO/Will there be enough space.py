##### https://www.codewars.com/kata/will-there-be-enough-space/train/python
"""
Bob is working as a bus driver. However, he has become extremely popular amongst the city's residents. 
With so many passengers wanting to get aboard his bus, he sometimes has to face the problem of not enough space left on the bus! 
He wants you to write a simple program telling him if he will be able to fit all the passengers.
"""

def enough(cap, on, wait):
    """
    This function accepts three parameters:
    cap   => is the amount of people the bus can hold excluding the driver.
    on    => is the number of people on the bus excluding the driver.
    wait  => is the number of people waiting to get on to the bus excluding the driver.
    If there is enough space, the function returns 0, 
    and if there isn't, the function returns the number of passengers he can't take.
    """
    cap_free = cap - on
    if cap_free >= wait:
        return 0    # The bus can fit all passengers
    return wait - cap_free  # The bus can't fit 'n' passengers (of the all waiting)

print(enough(10,5,5))       # 0     (He can fit all 5 passengers)
print(enough(100,60,50))    # 10    (He can't fit 10 of the 50 waiting)