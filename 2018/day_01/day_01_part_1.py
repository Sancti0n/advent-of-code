with open('2018/day_01/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

v = 0
for i in range(len(lines)):
    v += int(lines[i].split('\n')[0])
print(v)