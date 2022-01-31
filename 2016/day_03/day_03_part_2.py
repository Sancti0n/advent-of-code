with open('2016/day_03/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

t = []
temp = []
for i in lines:
    w = ''
    for a in i:
        if a != ' ': w += str(a)
        if a == ' ' and w != '':
            t.append(int(w))
            w = ''
        if a == '\n': t.append(int(w.split('\n')[0]))
    temp.append(t)
    t = []

l = len(temp)
a, b, c, pas = 0, 1, 2, 0
while c<l:
    while pas<3:
        t.append(temp[a][pas])
        t.append(temp[b][pas])
        t.append(temp[c][pas])
        pas += 1
    a += 3
    b += 3
    c += 3
    pas = 0

pos, c = 0, 0
t2 = []
while pos+2<len(t):
    t2.append(t[pos])
    t2.append(t[pos+1])
    t2.append(t[pos+2])
    t2.sort()
    if t2[0]+t2[1]>t2[2]: c += 1
    t2 = []
    pos += 3
print(c)