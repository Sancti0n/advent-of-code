with open('2015/day_02/list.txt', encoding="utf-8") as f:
    lines = f.readlines()
value = 0
for i in range(len(lines)):
    a = (lines[i].split('\n')[0]).split('x')
    for b in range(len(a)):
        a[b] = int(a[b])
    a.sort()
    value += 2*(int(a[0])+int(a[1])) + int(a[0])*int(a[1])*int(a[2])
print(value)