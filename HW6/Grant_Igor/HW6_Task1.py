def largest_number(*args):
    # Function returns the larges number
    return max(*args)
num_count = int(input("How many numbers are there? "))
print(largest_number(*[int(input("Enter your numbers: ")) for i in range(num_count)]))
