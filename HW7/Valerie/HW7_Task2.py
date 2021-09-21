import re

password = True
while password:
    password = input("Please, enter the password:")

    pw_low = re.search("[a-z]", password)
    pw_upper = re.search("[A-Z]", password)
    pw_num = re.search("[0-9]", password)
    pw_sign = re.search("[$#@]", password)
    pw_len = 6<= len(password) <=16 

    if pw_low and pw_upper and pw_num and pw_sign and pw_len:
        print("Valid password. Welcome to the website!")
        password = False
    else:
        print("Invalid password. Try again.")