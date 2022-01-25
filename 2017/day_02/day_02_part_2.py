with open('2017/day_02/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

v = 0
for i in lines:
    t = i.split('\t')
    t[len(t)-1] = t[len(t)-1].split('\n')[0]
    t.sort(key=int)
    for a in range(len(t)):
        for b in range(len(t)):
            if int(t[a])%int(t[b]) == 0 and t[a]!=t[b]:
                v += int(int(t[a])/int(t[b]))
                break
print(v)