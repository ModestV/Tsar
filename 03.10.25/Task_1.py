a = 'АБВГДЕЖЗИЙКЛМНОПРСТУФЧЦЧШЩЪЫЬЭЮЯ'.lower()
b = 'abcdefghijklmnopqestuvwxyz'
c = input('Введите чудестный текст: ').lower()
d = int(input('Введите чудестный сдвиг: '))

new_c = ''
for i in c:
    if i in a:
        index_for_a = a.find(i)+d
        if index_for_a > 31:
            index_for_a-=32
            new_c = new_c + a[index_for_a]
        else: 
            new_c = new_c + a[index_for_a]
    elif i in b:
        index_for_b = b.find(i)+d
        if index_for_b > 24: 
            index_for_b-=26
            new_c = new_c + b[index_for_b]
        else: 
            new_c = new_c + b[index_for_b]
    else:
        new_c = new_c + i
print(new_c)
