with open('2017/day_02/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

v = 0
for i in lines:
    t = i.split('\t')
    t[len(t)-1] = t[len(t)-1].split('\n')[0]
    t.sort(key=int)
    v += int(t[len(t)-1]) - int(t[0])
print(v)