# Function will reverse given list
# Input elements are separated by space
def rev_list():
    user_list = (input("Enter your elements split by space: ")).split()
    user_list.reverse()
    return user_list
print(rev_list())