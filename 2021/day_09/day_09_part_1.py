with open('2021/day_09/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].split('\n')[0]

def comparaison(a,b,c,d):
    if lines[a][b]<lines[c][d]: return True
    else: return False

def addV(i,a,t):
    t.append(lines[i][a])

t = []
for i in range(len(lines)):
    for a in range(len(lines[i])):
        if i>0 and i<len(lines)-1:
            if a+1<len(lines[i]):
                if a>0:
                    if comparaison(i,a,i,a+1) and comparaison(i,a,i,a-1) and comparaison(i,a,i-1,a) and comparaison(i,a,i+1,a): addV(i,a,t)
                if a==0:
                    if comparaison(i,a,i,a+1) and comparaison(i,a,i-1,a) and comparaison(i,a,i+1,a): addV(i,a,t)
            if a+1==len(lines[i]):
                if comparaison(i,a,i,a-1) and comparaison(i,a,i-1,a) and comparaison(i,a,i+1,a): addV(i,a,t)
        if i==0:
            if a+1<len(lines[i]):
                if a>0:
                    if comparaison(i,a,i,a+1) and comparaison(i,a,i,a-1) and comparaison(i,a,i+1,a): addV(i,a,t)
                if a==0:
                    if comparaison(i,a,i,a+1) and comparaison(i,a,i+1,a): addV(i,a,t)
            if a+1==len(lines[i]):
                if comparaison(i,a,i,a-1) and comparaison(i,a,i+1,a): addV(i,a,t)
        if i==len(lines)-1:
            if a+1<len(lines[i]):
                if a>0:
                    if comparaison(i,a,i,a+1) and comparaison(i,a,i,a-1) and comparaison(i,a,i-1,a): addV(i,a,t)
                if a==0:
                    if comparaison(i,a,i,a+1) and comparaison(i,a,i-1,a): addV(i,a,t)
            if a+1==len(lines[i]):
                if comparaison(i,a,i,a-1) and comparaison(i,a,i-1,a): addV(i,a,t)

count = 0
for nb in t:
    count += int(nb)+1
print(count)
