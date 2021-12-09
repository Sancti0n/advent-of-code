with open('2021/day_06/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

lines = lines[0].split(',')

a = 0
while a<80:
    for i in range(len(lines)):
        if lines[i] == '0':
            lines[i] = '6'
            lines.append('8')
        else: lines[i] = str(int(lines[i]) - 1)
    a += 1

print(len(lines))