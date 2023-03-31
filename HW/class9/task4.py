"""
Напишите функцию cacluate, которая может принимать любое количество чисел и возвращать кортеж.

Первое значение кортежа - это среднее значение всех параметров, а второе значение - все числа, превышающие среднее значение.
Второе значение оформите в виде списка.
"""

def cacluate(*args):
    average_value = sum(args)/len(args)
    value = []
    for i in args:
        if i > average_value:
            value.append(i)
    return average_value, value

print(cacluate(1,15,3,5))