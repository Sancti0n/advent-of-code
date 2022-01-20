with open('2017/day_01/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

v = 0
for i in range(len(lines[0])):
    if i == 0: 
        if lines[0][0] == lines[0][len(lines[0])-1]: v += int(lines[0][0])
    else:
        if lines[0][i] == lines[0][i-1]: v += int(lines[0][i])
print(v)