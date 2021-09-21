from codecs import decode
from this import s

zen = decode(s, "rot13")
print("******************************")
zen_reserve = zen #сделал копию текста перед поднятием всех букв в верх регистр
zen=zen.upper()
print(zen)
better_count = zen.count("BETTER")
never_count = zen.count("NEVER")
is_count = zen.count("IS")

print(f"Word 'better' in zen using  {better_count} times")
print(f"Word 'never' in zen using  {never_count} times")
print(f"Word 'is' in zen using  {is_count} times")

print("************************")
zen_reserve = zen_reserve.replace("i","&")
print(zen_reserve)

