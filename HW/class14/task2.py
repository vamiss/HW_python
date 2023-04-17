"""
Напишите программу создающую еще 1 .txt файл и запишите туда строку "но у меня не получается".
Создайте еще 1 .txt файл в котором будет объединение этого файла с файлом с предыдущего задания.
"""

with open('task21.txt', 'w+') as f:
    f.write(', но у меня не получается')

with open('task1.txt', 'r') as first, open('task21.txt', 'r') as second, open('task22.txt', 'w+') as third:
    third.write(first.read())
    third.write(second.read())