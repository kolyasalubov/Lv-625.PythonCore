# запитуємо користувача площу якої фігури він хоче обчислити

import Task1_module1

operator = input('Задайте першу літеру назви фігури (наприклад, к - коло), для якої необхідно обчислити площу: ')
try :
    if operator not in ['п', 'т', 'к'] :
        print("Доступні назви фігур 'п - прямокутник', 'т - трикутник', 'к - коло'")
    else :
        if operator == 'п':
            print("Введіть довжину однієї сторони прямокутника: ")
            a = float(input())
            print("Введіть довжину другої сторони прямокутника: ")
            b = float(input())
            print(Task1_module1.sqRectangle(a, b))
        elif operator == 'т':
            print("Введіть довжину однієї сторони трикутника: ")
            a = float(input())
            print("Введіть довжину другої сторони трикутника: ")
            b = float(input())
            print(Task1_module1.sqTriangle(a, b))
        elif operator == 'к':
            print("Введіть радіус кола: ")
            r = float(input())
            print(Task1_module1.sqCircle(r))
except :
    print('Not correct number!')

