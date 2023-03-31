database = {}

def writeStudent(name, count):
    database[name] = count

def findStudent(name):
    print(database[name])

writeStudent(name = input('Имя: '), count = input('Число: '))

findStudent(name = input('Имя: '))