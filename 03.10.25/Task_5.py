numbers = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000,
}
print("Выбирите действие:\n2. Перевод числа из Арабской с.с. в Римскую с.с.\n1. Перевод числа из Римской с.с в Арабскую с.с.")
answer = input()
if answer == '1':
    l = []
    n = input("Введите число в Римской с.с.: ").upper()
    r = 0
    for a in n:
        if a in numbers:
            l.append(numbers[a])
    for i in range(len(l)-1):
        if l[i]>=l[i+1]:
            r=r+l[i]
        else:
            r=r-l[i]
    r = r + l[-1]
    print(f'Число {n} в римской с.с. равно {r} в арабской с.с.')
if answer == '2':
    p = 1
    l_new = []
    l = []
    n = input("Введите число в Арабской с.с.: ")
    for i in range(-1,-len(n)-1,-1):
        r = int(n[i])
        if p==1:
            if r==9:
                l.append('IX')
            elif r>5 and r<9:
                l.append('V'+'I'*(r-5))
            elif r==5:
                l.append('V')
            elif r==4:
                l.append('IV')
            else:
                l.append('I'*(r))
            p+=1
        elif p==2:
            if r==9:
                l.append('XC')
            elif r>5 and r<9:
                l.append('L'+'X'*(r-5))
            elif r==5:
                l.append('L')
            elif r==4:
                l.append('XL')
            else:
                l.append('X'*(r))
            p+=1
        elif p==3:
            if r==9:
                l.append('CM')
            elif r>5 and r<9:
                l.append('D'+'C'*(r-5))
            elif r==5:
                l.append('D')
            elif r==4:
                l.append('CD')
            else:
                l.append('C'*(r))
            p+=1
        elif p==4:
            l.append('M'*int(n[:-3]))
            break
    for a in range(-1,-len(l)-1,-1):
        l_new.append(l[a])
    print(f'Число {n} в арабской с.с. равно {"".join(l_new)} в римской с.с.')
