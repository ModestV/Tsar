"""
1. [V] Нижний регистр
2. [X] Верхний регистр
3. [V] Специальные символы
4. [X] Цифры
5. [5] Длина пароля
"""
def show_settings():
    print(f'1. {l[0][0]} {l[0][1]}')
    print(f'2. {l[1][0]} {l[1][1]}')
    print(f'3. {l[2][0]} {l[2][1]}')
    print(f'4. {l[3][0]} {l[3][1]}')
    print(f'5. {l[4][0]} {l[4][1]}')
    print('0. Закончить настройку')

l = [
    ['[ ]','Нижний регистр'],
    ['[ ]','Верхний регистр'],
    ['[ ]','Специальные символы'],
    ['[ ]','Цифры'],
    ['[ ]','Длина пароля']
]

settings = [False,False,False,False,None]

print('Генератор паролей Pro Max.')

while 1:
    print('Укажите желаемые настройки пароля.')
    show_settings()
    answer = input('')
    if answer == '0':
        if any(settings):
            break
    elif answer == '1':
        if settings[0]==True:
            settings[0] = False
            l[0][0] = '[X]'
        else:
            settings[0]=True
            l[0][0] = '[V]'
    elif answer == '2':
        if settings[1] == True:
            settings[1] = False
            l[1][0] = '[X]'
        else:
            settings[1] = True
            l[1][0] = '[V]'
    elif answer == '3':
        if settings[2] == True:
            settings[2] = False
            l[2][0] = '[X]'
        else:
            settings[2] = True
            l[2][0] = '[V]'
    elif answer == '4':
        if settings[3] == True:
            settings[3] = False
            l[3][0] = '[X]'
        else:
            settings[3] = True
            l[3][0] = '[V]'
    elif answer == '5':
        password_len = int(input('Введите длину пароля: '))
        settings[4]=password_len
        l[4][0] = f'[{password_len}]'
    # print(settings)

if settings[4]==None:
    print('Введите длину пароля!')
    password_len = int(input('Длина пароля: '))
    settings[4] = password_len
    l[4][0] = f'[{password_len}]'

v = 'qwertyuiopasdfghjklzxcvbnm'
V = 'QWERTYUIOPASDFGHJKLZXCVBNM'
spec = '!@#$%^&*'
dig = '0123456789'
symbols = ''

if settings[0]==True:
    symbols = symbols + v
if settings[1]==True:
    symbols = symbols + V
if settings[2]==True:
    symbols = symbols + spec
if settings[3]==True:
    symbols = symbols + dig


import random
password = random.choices(symbols,k=settings[4])

Pass = [False,False,False,False]
while 1:
    print(1)
    for i in password:
        if settings[0]==True:
            if Pass[0]==False:
                if i in V:
                    Pass[0] = True
        if settings[1]==True:
            if Pass[1]==False:
                if i in v:
                    Pass[1] = True
        if settings[2]==True:
            if Pass[2]==False:
                if i in spec:
                    Pass[2] = True
        if settings[3]==True:
            if Pass[3]==False:
                if i in dig:
                    Pass[3] = True
    if all(Pass):
        print('0'.join(password))
        break
    else:
        password = random.choices(symbols, k=settings[4])
