while True:
    action = input("Введите 'game' для запуска игры 'Угадай число' или 'off' для выхода: ")
    if action == "off":
        print("Программа завершена.")
        break
    elif action == "game":
        print("Добро пожаловать в игру 'Угадай число'! У вас есть 3 попытки.")
        secret_number = 3
        attempts = 3
        while attempts > 0:
            guess = int(input("Угадайте число от 1 до 10: "))
            if guess == secret_number:
                print("Вы выиграли билет на концерт!")
                break
            elif guess < secret_number:
                print("Загаданное число больше!")
            else:
                print("Загаданное число меньше!")
            attempts -= 1
        else:
            print("Вы проиграли. Было загадано число", secret_number)