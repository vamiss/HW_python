def is_date_is_magic(date):
    spl_date = date.split('.')
    return int(spl_date[0]) * int(spl_date[1]) == int(str(f'{spl_date[2][2]}{spl_date[2][3]}'))

print(is_date_is_magic(date = input()))
