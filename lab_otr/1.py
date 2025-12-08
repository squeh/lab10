password = "admin"
attempts = 1
att = 3

while True:
    passw = input(f"Введите пароль, у вас {att} попытка(-и): ")
    if passw == password:
        print("Пароль верный! Вы вошли в систему.")
        break
    if attempts > 2:
        print("Вход заблокирован.")
        break
    attempts += 1
    att -= 1
