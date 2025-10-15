# №4
a = input("Введите строку: ").lower()
dict = {}
for i in a:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

b = []

for i, count in dict.items():
    b.append((i, count))

for i in range(len(b)):
    for j in range(i + 1, len(b)):
        if b[i][1] < b[j][1]:
            b[i], b[j] = b[j], b[i]
top = b[:3]
if top:
    for c in range(len(top)):
        d, count = top[c]
        print(f"Символ '{d}': {count} раз")
