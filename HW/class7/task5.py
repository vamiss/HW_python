"""
Каждый из N школьников некоторой школы знает M языков.
Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
Входные данные:
Сначала запрашивается количество учеников(например 6).
Дальше запрашивается количество учеников знающих определенный набор языков и языки которые они знают
Например:
3
Russian
English
Japanese
2
Russian
English
1
English
Вывод должен быть:
3 - [Russian, English,Japenese]
1 - [English]
"""

n = int(input())  # количество учеников
languages = []  # языки, которые знают ученики
for i in range(n):
    m = int(input())  # количество языков, которые знает i-й ученик
    languages.append(set(input().split()))  # множество языков, которые знает i-й ученик

# языки, которые знают все ученики
intersection = set.intersection(*languages)
print(len(intersection), '-', sorted(list(intersection)))

# языки, которые знает хотя бы один ученик
union = set.union(*languages)
print(len(union), '-', sorted(list(union)))