dal = float(input('Введите дальность: '))

if dal > 28 and dal < 30:
    print('ПОПАЛ')
elif dal >= 30:
    print('ПЕРЕЛЕТ')
elif dal > 0 and dal <= 28:
    print('НЕДОЛЕТ')
elif dal <=0:
    print('НЕ БЕЙ ПО СВОИМ!!!')