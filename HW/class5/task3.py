grades = input("Введите оценки студента через пробел: ")

grades_list = grades.split()
fives = grades_list.count('5')
total_grades = len(grades_list)
fives_percentage = fives / total_grades * 100

print("Количество пятёрок:", fives)
print("Общее количество оценок:", total_grades)
print("Процент пятёрок:", fives_percentage)