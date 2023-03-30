marks = input("Введите список оценок через запятую: ").split(",")
marks = [int(mark) for mark in marks]

fives = marks.count(5)
fours = marks.count(4)
threes = marks.count(3)

print("Список оценок:", marks)
print("Количество пятёрок:", fives)
print("Количество четвёрок:", fours)
print("Количество троек:", threes)

total_marks = len(marks)
success_rate = (fives + fours + threes) / total_marks * 100

print("Успеваемость:", success_rate)