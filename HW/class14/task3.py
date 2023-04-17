# -*- coding: utf-8 -*-

"""
Напишите программу, которая будет считывать содержимое файла, добавлять к считанным строкам порядковый номер и сохранять их в таком
виде в новом файле. Имя исходного файла необходимо запросить у пользователя, так же, как и имя целевого файла. Каждая строка в созданном
файле должна начинаться с ее номера, двоеточия и пробела, после чего
должен идти текст строки из исходного файла.
"""

name = input('Введите имя исходного файла: ')

with open('FileforTask3.txt', 'r') as f_for, open(f'{name}.txt', 'w+') as f_name:
    for i, line in enumerate(f_for):
        f_name.write(f'{i+1}: {line}')