cap = int(input("Enter amount of people the bus can hold : ")) 
on = int(input("Enter number of people  sit in bus: "))
wait = int(input("Enter number of people  waiting  to get in bus: "))
def enough(cap, on, wait):
    if cap - on - wait >= 0:
        return 0 
    else:
        amount = cap - on - wait
        return (f"Unfortunately {abs(amount)} passenger can`t sit in the bus")
work = enough(cap, on, wait)
print(work)
