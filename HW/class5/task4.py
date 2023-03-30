personal_info = []

surname = input("Введите фамилию преподавателя: ")
position = input("Введите должность: ")
students_count = input("Введите количество студентов во всех группах через запятую (например: 12,8,10): ")

personal_data = [surname, position, students_count.split(",")]
personal_info.append(personal_data)

print("Личная информация записана успешно.")
print("Общий список с информацией: ")
print(personal_info)
