with open('2021/day_09/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].split('\n')[0]

t = []
for i in range(len(lines)):
    for a in range(len(lines[i])):
        if i>0 and i<len(lines)-1:
            if a+1<len(lines[i]):
                if a>0:
                    if lines[i][a]<lines[i][a+1] and lines[i][a-1]>lines[i][a] and lines[i-1][a]>lines[i][a] and lines[i+1][a]>lines[i][a]: t.append(lines[i][a])
                if a==0:
                    if lines[i][a]<lines[i][a+1] and lines[i][a]<lines[i-1][a] and lines[i][a]<lines[i+1][a]: t.append(lines[i][a])
            if a+1==len(lines[i]):
                if lines[i][a]<lines[i][a-1] and lines[i][a]<lines[i-1][a] and lines[i][a]<lines[i+1][a]: t.append(lines[i][a])
        if i==0:
            if a+1<len(lines[i]):
                if a>0:
                    if lines[i][a]<lines[i][a+1] and lines[i][a]<lines[i][a-1] and lines[i][a]<lines[i+1][a]: t.append(lines[i][a])
                if a==0:
                    if lines[i][a]<lines[i][a+1] and lines[i][a]<lines[i+1][a]: t.append(lines[i][a])
            if a+1==len(lines[i]):
                if lines[i][a]<lines[i][a-1] and lines[i][a]<lines[i+1][a]: t.append(lines[i][a])
        if i==len(lines)-1:
            if a+1<len(lines[i]):
                if a>0:
                    if lines[i][a]<lines[i][a+1] and lines[i][a]<lines[i][a-1] and lines[i][a]<lines[i-1][a]: t.append(lines[i][a])
                if a==0:
                    if lines[i][a]<lines[i][a+1] and lines[i][a]<lines[i-1][a]: t.append(lines[i][a])
            if a+1==len(lines[i]):
                if lines[i][a]<lines[i][a-1] and lines[i][a]<lines[i-1][a]: t.append(lines[i][a])

count = 0
for nb in t:
    count += int(nb)+1
print(count)
