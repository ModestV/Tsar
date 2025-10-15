def f(x):
    s = set()
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            s.add(i)
            s.add(x//i)
    return sorted(s)
MaxNOD = -1
# print(f(1260))
# print(f(3400))
a = f(int(input("Введите первое число (1260): ")))
b = f(int(input("Введите второе число (3400): ")))
for i in a:
    if i in b:
        if MaxNOD < i: MaxNOD = i
print(MaxNOD)
