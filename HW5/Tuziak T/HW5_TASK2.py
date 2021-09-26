def login_check (login: str):
    while login != "Перший":
        return "Спробуйте ще раз. ваш логін неправильний"
    else:
        return "Вітаємо! Ви успішно залогінились"

print(login_check("Second"))
print(login_check("First"))