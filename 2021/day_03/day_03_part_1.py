with open('2021/day_03/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

longueur = len(lines[0])
a, zero, one = 0, 0, 0
gamma = ''
epsilon = ''

while a<longueur-1:
    for i in lines:
        if i[a] == '0': zero += 1
        else: one += 1
    if zero>one: gamma += '0'
    else: gamma += '1'
    zero, one = 0, 0
    a += 1

for i in gamma:
    if i == '1': epsilon += '0'
    else: epsilon += '1'

print(int(gamma, 2)*int(epsilon, 2))