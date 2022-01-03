with open('2021/day_08/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].split('\n')[0]

def strIn(a,b):
    c = 0
    for i in range(len(a)):
        if a[i] in b: c+=1
    if len(a) == c: return True
    else: return False

def strOut(a,b):
    v = ''
    for i in range(len(a)):
        if a[i] not in b: v += a[i]
    for i in range(len(b)):
        if b[i] not in a: v+= b[i]
    return v

def strSort(a):
    for c in range(len(a)):
        a[c] = ''.join(sorted(a[c]))
    return a

def select(arr):
    d = {}
    for i in range(len(arr)):
        if len(arr[i]) == 2: d[1] = arr[i]
        if len(arr[i]) == 3: d[7] = arr[i]
        if len(arr[i]) == 4: d[4] = arr[i]
        if len(arr[i]) == 7: d[8] = arr[i]
        if len(arr[i]) == 6:
            if strIn(d[4], arr[i]): d[9] = arr[i]
            elif strIn(d[1], arr[i]): d[0] = arr[i]
            else: d[6] = arr[i]
        if len(arr[i]) == 5:
            if strIn(d[1], arr[i]): d[3] = arr[i]
            elif strIn(strOut(d[4], d[7]), arr[i]): d[5] = arr[i]
            else: d[2] = arr[i]
    return d

t = []

for i in lines:
    a = (i.split(' |')[0]).split(' ')
    b = (i.split('| ')[1]).split(' ')
    a.sort(key=len)
    d = select(strSort(a))
    strSort(b)
    v = ''
    for w in b:
        k = list(d.keys())
        val = list(d.values())
        v += str(k[val.index(w)])
    t.append(v)

v = 0
for i in t:
    v += int(i)
print(v)