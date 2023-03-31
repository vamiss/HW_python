"""
Имеется список с произвольными значениями. Нужно преобразовать его во множество и проверить
являются ли все его элементы неизменяемыми.
Вывести True или False. И изменяемые элементы
Подсказка: чтобы узнать тип элемента можно использовать функцию type()
"""
testList = [1,2,2,[3,4],(1,2,3),"1",{1,2,3}]

testSet = set(testList)
print(testSet)

changeable = False
for element in testSet:
    if type(element) in [list, dict, set]:
        print(element, "is changeable")
        changeable = True

if changeable:
    print(False)
else:
    print(True)