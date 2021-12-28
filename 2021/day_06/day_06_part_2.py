with open('2021/day_06/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

lines = list(map(int,lines[0].split(',')))

d, t = {}, []
for x in lines:
    if x in d: d[x] += 1
    else: d[x] = 1
for i in range(0,9):
    if i in d: t.append(d[i])
    else: t.append(0)

a, m, count = 0, 0, 0
while a<256:
    m = t[0]
    for n in range(len(t)):
        if n>0: t[n-1] = t[n]
    t[6] += m
    t[8] = m
    a += 1

for a in t: count += a
print(count)