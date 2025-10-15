a = [1, 2, 3, 4, 5, 1, 1, 1, 4, 5, 2]
b = list(set(a))
for i in range(len(b)):
    print(b[i], a.count(b[i]))
