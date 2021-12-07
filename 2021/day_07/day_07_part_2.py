with open('2021/day_07/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

lines = list(map(int, lines[0].split(',')))

def sumN(n):
    return int(n*(n+1)/2)

maxFuel, a = 0, 0
t = []

while a<max(lines):
    for i in lines:
        maxFuel += sumN(abs(i-a))
    t.append(maxFuel)
    maxFuel = 0
    a+=1

print(min(t))