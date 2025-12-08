num = -9999999999
print("Самое большое число в введенной последовательности.")
while True:
    number = int(input("Введите число: "))
    if number > num and number != 0:
        num = number
    elif number == 0:
        print(f"Самое большое число, которое было: {num}")
        break
