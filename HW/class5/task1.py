games_list = []
game = input("Введите название настольной игры: ")

while game != '0':
    if game in games_list:
        print("Эта игра уже записана")
    else:
        games_list.append(game)
        games_list.sort()
    game = input("Введите название настольной игры: ")

print("Список игр:", games_list)