with open('2017/day_01/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

v = 0
s = int(len(lines[0])/2)
for i in range(s):
    if lines[0][i] == lines[0][i+s]: v += int(lines[0][i])*2
print(v)