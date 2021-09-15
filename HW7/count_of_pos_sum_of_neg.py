def num_of_pos():
    numbers = input("Enter your numbers separated by space: ").split()
    numbers_int = int(numbers)
    num, start = 0, 0
    while num < len(numbers_int):
        if numbers_int[num] > 0:
            start += 1
        return start

print(num_of_pos())