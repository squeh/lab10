total = 0

while True:
    price = int(input("Введите цену товара: "))

    if price == 0:
        break

    if price < 0:
        print("Ошибка цены")
        continue

    total += price

if total > 1000:
    discount = total * 0.1
    total -= discount
    print(f"Применена скидка 10%: {int(discount)} руб.")

print(f"Итоговая сумма к оплате: {int(total)} руб.")
