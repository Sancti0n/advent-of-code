with open('2016/day_03/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

t = []
c = 0
for i in lines:
    w = ''
    for a in i:
        if a != ' ': w += str(a)
        if a == ' ' and w != '':
            t.append(int(w))
            w = ''
        if a == '\n': t.append(int(w.split('\n')[0]))
    t.sort()
    if t[0]+t[1]>t[2]: c += 1
    t = []
print(c)