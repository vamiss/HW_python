print("Введите свой отзыв или 'off', чтобы выйти: ")
while True:
    review = input()
    if review.lower() == "off":
        print("Система предпочтений настроена")
        break
    else:
        print("Спасибо, ваш отзыв принят!")
