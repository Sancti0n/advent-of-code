with open('2019/day_01/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

v = 0
for i in range(len(lines)):
    a = int(lines[i].split('\n')[0])
    while (a/3 - 2) >= 1:
        v += int(a/3) - 2
        a = int(a/3) - 2
print(v)