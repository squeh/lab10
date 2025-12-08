# НЕ ДОДЕЛАНО

cost = []

while True:
    cosst = int(input("Введите цену товара: ")).append()
    if cosst < 0:
        print("Ошибка цены.")
        continue
    elif cost > 1000:
        cost %= 0.1
    elif cosst == 0:
        print(f"Сумма товаров: {cost}")
        break
