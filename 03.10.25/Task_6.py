def TheHanged():
    print("".join(l[0]))
    print("".join(l[1]))
    print("".join(l[2]))
    print("".join(l[3]))
    print("".join(l[4]))
    print("".join(l[5]))
    print("".join(l[6]))
" _______  "
"  |/   |  "
"  |    o  "
"  |   /0\\"
"  |   /'\\"
"  |       "
" ‾‾‾‾‾    "

l = [
    [" "," "," "," "," "," "," "," "," "," "],
    [" "," ","|"," "," "," "," "," "," "," "],
    [" "," ","|"," "," "," "," "," "," "," "],
    [" "," ","|"," "," "," "," "," "," "," "],
    [" "," ","|"," "," "," "," "," "," "," "],
    [" "," ","|"," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "," "," "]
]

alphabet = ['йцукенгшщзхъфывапролджэячсмитьбюё']
n = input('Это игра Висельница!\n Загадайте слово: ').lower()
original = n
correct = "_"*len(n)
g = -2
k = 0
while correct != original or k<10:
    if correct == original:
        print(f"Поздравляем! Вы выиграли :)\n Угаданное слово - {original}")
        break
    answer = input("Угадайте букву: ").lower()
    print()
    g = -2

    if answer in n:
        while g!= -1:
            g = n.find(answer)
            if g == -1:
                break
            correct = correct[:g]+ answer +correct[g+1:]
            n = n[:g]+'_'+n[g+1:]
        print(correct, "Правильно!")
    else:
        print('Неправильно!')
        k+=1
        if k==1:
            l[6][1] = '‾'
            l[6][2] = '‾'
            l[6][3] = '‾'
            l[6][4] = '‾'
            l[6][5] = '‾'
        elif k == 2:
            l[0][1] = '-'
            l[0][2] = '-'
            l[0][3] = '-'
            l[0][4] = '-'
            l[0][5] = '-'
            l[0][6] = '-'
            l[0][7] = '-'
            l[0][8] = '-'
        elif k == 3:
            l[1][4] = '/'
        elif k == 4:
            l[1][8] = '|'
        elif k == 5:
            l[2][8] = 'o'
        elif k == 6:
            l[3][8] = '0'
        elif k == 7:
            l[3][7] = '/'
        elif k == 8:
            l[3][9] = '\\'
        elif k == 9:
            l[4][7] = '/'
        elif k == 10:
            l[4][8] = "'"
            l[4][9] = "\\"
            print(f'Вы проиграли :(\nПравильное слово - {original}')
            TheHanged()
            break
        TheHanged()
