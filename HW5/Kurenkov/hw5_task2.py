# Write a script that checks the login that the user enters.
# If the login is "First", then greet the users. If the login is different, send an error message.
# (need to use loop while)

input_login = input("Input login: ")
while input_login != "First":
    print("Please try again")
    input_login = input("Input login: ")
else:
    print("Hello, First")


