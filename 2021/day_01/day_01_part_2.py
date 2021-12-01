with open('2021/day_01/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

t = []
increase = 0

def resteNumber(a):
    while a%3 != 0: a-=1
    return a

for i in range(resteNumber(len(lines))):
    t.append(int(lines[i])+int(lines[i+1])+int(lines[i+2]))

for i in range(len(t)):
    if i>0:
        if int(t[i])>int(t[i-1]): increase+=1
print(increase)