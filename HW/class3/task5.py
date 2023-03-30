num = input()
asd = sum(map(int, str(num)))

if asd % 3 == 0 and int(num[-1]) % 2 == 0:
    print("Делится")
else:
    print("Не делится")