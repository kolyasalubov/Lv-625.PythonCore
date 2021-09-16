##### Home_Work5_Task_2 ("Collection" Slide 62)
"""
Write a script that checks the login that the user enters. 
If the login is "First", then greet the users. 
If the login is different, send an error message. 
(need to use loop while)
"""

def login_check (login: str):
    """
    This function checks the login that the user enters.
    """
    while login != "First":
        return "Try again. Your login is incorrect."
    else:
        return "Congratulations! You have successfully logged in."

print(login_check("Second"))
print(login_check("First"))

