l = []
n= int(input('Введите кол-во чисел в списке: '))
for z in range(n):
    l.append(int(input("Введите числа: ")))
n=0
for a in range(len(l)):
    for b in range(a+1,len(l)):
        for c in range(b+1,len(l)):
            if l[a]+l[b]+l[c] == 0:
                n+=1
if n>0:
    print('True')
else:
    print('False')
