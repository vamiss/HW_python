# Создайте функцию которая принимает на вход 3 именованных параметра, выведите на печать значения этих параметров,
# но только в том случае если они не равны None.

def named(first = None, second = None, third = None):
    if first is not None:
        print('first is', first)
    if second is not None:
        print('second is', second)
    if third is not None:
        print('third is', third)

named(first = 20, second = 10, third = 30)