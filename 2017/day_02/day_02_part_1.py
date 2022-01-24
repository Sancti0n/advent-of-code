with open('2017/day_02/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

v = 0
for i in lines:
    t = i.split('\t')
    t[len(t)-1] = t[len(t)-1].split('\n')[0]
    for a in range(len(t)):
        if a == 0:
            maximum = int(t[a])
            minimum = int(t[a])
        else:
            if int(t[a])>maximum: maximum = int(t[a])
            if int(t[a])<minimum: minimum = int(t[a])
    v += maximum - minimum
print(v)