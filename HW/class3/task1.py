quest1 = input('Прием пищи: ').lower()

if quest1 == 'завтрак':
    print('Каша')
else:
    quest2 = input('Вы хотите плотно поесть? ').lower()
    if quest2 == 'да':
        print('Плов')
    else:
        print('Котлета с пюре')