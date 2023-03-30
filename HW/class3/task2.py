cost = int(input('Summa: '))
time = int(input('Vremya: '))

if 9 < time < 13:
    print(cost / 2)
elif 20 < time < 22:
    print(cost / 4)
else:
    print(cost)