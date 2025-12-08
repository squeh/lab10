pincode = "4590"

while True:
    pin = input("Введите пин-код: ")
    if pin == pincode:
        print("Доступ разрешен.")
        break
    else:
        print("Ошибка. Попробуйте еще раз.")
