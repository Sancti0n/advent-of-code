with open('2021/day_02/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

h, d, aim = 0, 0, 0
for i in lines:
    if 'forward' in i:
        h += int(i.split('forward ')[1])
        d += int(i.split('forward ')[1])*aim
    if 'down' in i:
        aim += int(i.split('down ')[1])
    if 'up' in i:
        aim -= int(i.split('up ')[1])

print(d*h)