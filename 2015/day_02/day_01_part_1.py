with open('2015/day_02/list.txt', encoding="utf-8") as f:
    lines = f.readlines()
value = 0
for i in range(len(lines)):
    a = (lines[i].split('\n')[0]).split('x')
    t = []
    for c in range(len(a)):
        for d in range(c+1,len(a)):
            t.append(int(a[c])*int(a[d]))
    t.sort()
    value += 2*(int(a[0])*int(a[1]) + int(a[1])*int(a[2]) + int(a[2])*int(a[0])) + t[0]
print(value)