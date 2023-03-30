tovar1 = int(input())
tovar2 = int(input())
tovar3 = int(input())

if tovar1 > tovar2 > tovar3:
    print((tovar1 + tovar2 + tovar3) / 2)
elif tovar1 < tovar2 < tovar3:
    print((tovar1 + tovar2 + tovar3) / 3)
else:
    print(f'Сумма к оплате: {tovar1 + tovar2 + tovar3}')