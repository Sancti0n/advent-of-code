with open('2021/day_07/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

lines = list(map(int, lines[0].split(',')))

# Simple parcours

t = []
value, a = 0, 1
while a<max(lines):
    for i in range(len(lines)):
        value += abs(lines[i]-a)
    t.append(value)
    value = 0
    a += 1
print('Simple parcours :', min(t))

# Avec la médiane

lines.sort()
if len(lines)%2==0: mediane = lines[int(len(lines)/2)]
else: mediane = int((len(lines)/2)+int(len(lines)/2)+1)/2

value = 0
for i in range(len(lines)):
    value += abs(lines[i]-mediane)
print('Avec la médiane :', value)