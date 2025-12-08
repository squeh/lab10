num1 = int(input("Введите 1 число: "))

while True:
    num2 = int(input("Введите 2 число: "))
    if num2 > num1:
        break
    else:
        print("Введите число заново.")
while True:
    num3 = int(input("Введите 3 число: "))
    if num3 > num2:
        break
    else:
        print("Введите число заново.")
print("""
Последовательность принята.""")
