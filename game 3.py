import random

print("Угадай число от 1 до 10!")

while True:
    num = random.randint(1, 10)
    num1 = int(input("Твоя попытка: "))

    if num1 == num:
        print("Угадал!")
    elif num1 > num:
        print("Слишком много!")
    else:
        print("Слишком мало!")

    restart = input("Ещё раз? (да/нет): ")
    if restart == "нет":
        print("Пока!")
        break