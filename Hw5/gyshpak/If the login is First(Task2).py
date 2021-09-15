my_str = ""
while my_str != "First":
    my_str = str(input("Enter yor login "))
    print("Greet you, your logon is true" if my_str == "First" else f"login {my_str} is faild, train again")
