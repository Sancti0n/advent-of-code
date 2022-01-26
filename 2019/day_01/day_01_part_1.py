with open('2019/day_01/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

v = 0
for i in range(len(lines)):
    v += int(int(lines[i].split('\n')[0])/3) - 2
print(v)