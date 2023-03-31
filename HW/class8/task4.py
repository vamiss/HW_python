# Напишите программу считающую и обрабатывающую индекс массы тела.
# В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
# от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
# Формула определения ИМТ: index = weight / (height * height)

def index(weight:float, height:float):
    index = weight / (height ** 2)
    return index
def result(index: float):
    if index < 18.5:
        print('Недостаточный вес')
    elif 18.5 < index < 25:
        print('ИМТ в норме')
    elif index > 25:
        print('Избыточный вес')
weight = float(input('Введите вес: '))
height = float(input('Введите рост: '))
index = index(weight, height)
result(index)