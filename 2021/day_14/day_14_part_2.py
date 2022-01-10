with open('2021/day_14/list.txt', encoding="utf-8") as f:
    x, lines = f.read().split('\n\n')

lines = lines.split('\n')

d = {}
for i in lines:
    d[i.split(' -> ')[0]] = i.split(' -> ')[1]

f = {}
i = 0
while i+1<len(x):
    w = x[i]+x[i+1]
    if w in f: f[w] += 1
    else: f[w] = 1
    i+=1

for i in d:
    if i not in f: f[i] = 0

n = {}
for i in f:
    if i[0] not in n: n[i[0]] = 0
    if i[1] not in n: n[i[1]] = 0
for i in x: 
    n[i] += 1

def poly(d,f,a):
    a1 = 0
    while a1<a:
        temp = f.copy()
        t = {}
        for i in f:
            if f[i]>0: t[i] = f[i]
        for i in t:
            f1 = i[0]+d[i]
            f2 = d[i]+i[1]
            temp[f1] += f[i]
            temp[f2] += f[i]
            temp[i] -= f[i]
            n[d[i]] += f[i]
        f = temp.copy()
        a1 += 1
    return n,f

value = poly(d,f,40)[0]
maximum, minimum = 0, 0
for i in value:
    if maximum == 0: minimum = value[i]
    if maximum<value[i]: maximum = value[i]
    if minimum>value[i]: minimum = value[i]
print(maximum-minimum)