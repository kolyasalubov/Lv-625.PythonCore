import re

password = str(input("Enter your password: "))


while True:
    pattern_1 = re.findall("[a-z]", password)
    pattern_2 = re.findall("[A-Z]", password)
    pattern_3 = re.findall("[0-9]", password)
    pattern_4 = re.findall("[@#$]", password)


    if pattern_1 and pattern_2 and pattern_3 and pattern_4 and len(password) >= 6 and len(password) <= 16:
        print("Valid password")
        break
    else:
        password = str(input("Invalid pass, please enter new password: "))
