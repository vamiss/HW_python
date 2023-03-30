while True:
    price = float(input("Введите стоимость товара (или 0 для выхода): "))
    if price == 0:
        print("Программа завершена.")
        break
    discount = price * 0.1  # скидка в 10%
    price_with_discount = price - discount
    print("Цена со скидкой: ", price_with_discount)
