with open('2015/day_12/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

t = lines[0].split('":')
somme = 0

for i in t:
    a = 0
    while a < len(i):
        if i[a] == '-' or i[a].isdigit():
            v = i[a]
            a += 1
            while i[a].isdigit():
                v += i[a]
                a += 1
            somme += int(v)
        else:
            a += 1
print(somme)