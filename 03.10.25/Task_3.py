def print_pack_report(count1):
    while count1>1:
        if (count1%3 == 0) and (count1%5 == 0):
            return print(f'{count1} - расфасуем по 3 или по 5')
        elif (count1%3 == 0) and (not(count1%5 == 0)):
            return print(f'{count1} - расфасуем по 5')
        elif (not(count1%3 == 0)) and (count1%5 == 0):
            return print(f'{count1} - расфасуем по 3')
        else:
            return print(f'{count1} - не заказываем!')
    print_pack_report(count-1)
print(print_pack_report(3))
