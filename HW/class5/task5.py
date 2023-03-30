lst = [0, 1, 2, 3, 4]
n = len(lst)
if n <= 1:
    print("Нет")
else:
    for i in range(1, n):
        if lst[i] <= lst[i-1]:
            print("Нет")
            break
    else:
        print("Да")