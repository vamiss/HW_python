"""
Напишите генератор выводящий все символы строки на печать, но только в том случае,
если они являются буквами (остальные игнорируются).
"""

def findLetters_gen(my_string):
    for i in my_string:
        if i.isalpha():
            yield i

for j in findLetters_gen(my_string = input()):
    print(j)