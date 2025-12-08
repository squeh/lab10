start = 1

while True:
    num = int(input("Введите число: "))
    if num < 0:
        break
    if num > 0:
        start *= num

print(start)
