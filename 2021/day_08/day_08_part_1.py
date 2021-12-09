with open('2021/day_08/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = (lines[i].split(' | ')[1]).split('\n')[0]

t = ['']
count = 0
for i in range(len(lines)):
    t = lines[i].split(' ')
    for a in t:
        if len(a) == 2 or len(a) == 3 or len(a) == 4 or len(a) == 7: count += 1
print(count)