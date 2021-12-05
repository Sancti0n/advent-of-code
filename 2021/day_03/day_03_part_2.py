with open('2021/day_03/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

tmax = []
tmin = []
t = []
for i in range(len(lines)):
    tmax.append(lines[i].split('\n')[0])
    tmin.append(lines[i].split('\n')[0])

def maxValue(t, a):
    tValue = [0,0]
    for i in range(len(t)):
        #print(a)
        if t[i][a] == '0': tValue[0] += 1
        else: tValue[1] += 1
    if tValue[0] == tValue[1]: maxV = 1
    else: maxV = tValue.index(max(tValue))
    return maxV

def minValue(t, a):
    tValue = [0,0]
    for i in range(len(t)):
        if t[i][a] == '0': tValue[0] += 1
        else: tValue[1] += 1
    if tValue[0] == tValue[1]: minV = 0
    else: minV = tValue.index(min(tValue))
    return minV

def life(tmax, tmin):
    b = 0
    while len(tmax) != 1 and b<12:
        l = 0
        if b == 0: maxV = str(maxValue(tmax, b))
        while l<len(tmax):
            if tmax[l][b] != maxV:
                del tmax[l]
                l -= 1
            l+=1
        if b<11:
            b += 1
            maxV = str(maxValue(tmax, b))
    t.append(tmax[0])

    b = 0
    while len(tmin) != 1:
        l = 0
        if b == 0: minV = str(minValue(tmin, b))
        while l<len(tmin):
            if tmin[l][b] != minV:
                del tmin[l]
                l -= 1
            l+=1
        b += 1
        minV = str(minValue(tmin, b))
    t.append(tmin[0])

life(tmax,tmin)
print(int(t[0],2)*int(t[1],2))