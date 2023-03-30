"""Создайте словарь с количеством элементов не менее 5-ти.
Поменяйте местами первый и последний элемент объекта.
Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value».
Выведите на печать итоговый словарь. Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
"""

my_dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

first_key, first_value = my_dict.popitem()
last_key, last_value = my_dict.popitem()
my_dict.update({last_key: last_value, first_key: first_value})

my_dict.pop(2)

my_dict.update({'new_key': 'new_value'})

print(my_dict)