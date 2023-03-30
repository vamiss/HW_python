categ = input('category: ').lower()

if categ == 'продукты':
    cost = int(input('cena: '))
    if cena < 100:
        print('vypechka')
    elif 100 <= cena < 500:
        print('orehi')
    else:
        print('fruits')
else:
    print('tovary dlya doma')