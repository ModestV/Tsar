def check_winners(scores,student_score):
    top3= (sorted(scores)[::-1])[:3]
    if student_score in scores:
        return('Вы в тройке победителей!')
    else:
        return('Вы не прошли в тройку победителей.')
a = int(input('Сколько участников? '))
l = []
for i in range(a):
    l.append(int(input('Введите бал участника: ')))
b = int(input('Введите ваш бал: '))
print(check_winners(l,b))
