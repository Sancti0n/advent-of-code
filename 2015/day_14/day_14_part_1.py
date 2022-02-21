with open('2015/day_14/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

def calcul(v, t, pause, d):
    q, pause = divmod(d, t + pause)
    distance = (q*t + min(pause, t))*v
    return distance

temp = []
t = []
d = 2503
for i in lines:
    arr = i.split(' ')
    for a in arr:
        if a.isdigit():
            temp.append(a)
    t.append(calcul(int(temp[0]), int(temp[1]), int(temp[2]), d))
    temp.clear()
print(max(t))