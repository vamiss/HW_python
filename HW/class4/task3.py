login = input("Введите логин: ")
restricted_chars = "=?*^$№@_"
restricted_chars_used = []

for char in login:
    if char in restricted_chars:
        restricted_chars_used.append(char)

if restricted_chars_used:
    print("Следующие запрещенные символы использовались в логине: ")
    print(', '.join(restricted_chars_used))
else:
    print("Запрещенных символов не было использовано в логине.")
