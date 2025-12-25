balance = 1000

while True:
    choice = input(f"""Выберите пункт меню: 
1. Узнать баланс
2. Снять 100 руб
3. Положить 100 руб
4. Выход
""")

    if choice == '1':
        print(f"Ваш текущий баланс: {balance}")

    elif choice == '2':
        if balance >= 100:
            balance -= 100
            print("Снято 100 рублей")
        else:
            print("Недостаточно средств")

    elif choice == '3':
        balance += 100
        print("Баланс пополнен на 100 рублей")

    elif choice == '4':
        print("До свидания!")
        break

    else:
        print("Неверная команда. Выберите еще раз")
