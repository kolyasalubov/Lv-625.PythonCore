import re

user_password=input("please enter your password: ")

def password_checker (up=user_password):
    if len(up)>=6 and len(up)<=16 and len(re.findall("[a-z]", up)) > 0 and len(re.findall("[A-Z]", up)) > 0 and len(re.findall("[0-9]", up)) > 0 and len(re.findall("[$#@]", up)) > 0:
        print("Welcome, password structure is valid")
    else:
        print("Sorry, password structure is not valid")

password_checker()