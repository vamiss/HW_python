"""
Дана строка чисел от 0 до 9 необходимо создать словарь где в качестве ключа будет цифра,
а в качестве значения количество этих цифр в строке
"""

string = "112334567890"

digit_counts = {}
for digit in string:
    if digit in digit_counts:
        digit_counts[digit] += 1
    else:
        digit_counts[digit] = 1

print(digit_counts)
