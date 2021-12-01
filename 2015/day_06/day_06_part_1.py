import re

t1 = []
t2 = []
i = 0
while i<1000:
    t2.append(False)
    i+=1

def setBool(cmd, value):
    if 'toggle' in cmd: return not value
    if 'turn on' in cmd: return True
    if 'turn off' in cmd: return False
'''
with open('2015/day_06/list.txt', encoding="utf-8") as f:
    for line in f:
        commands = re.findall(r'turn on|turn off|toggle', line)
        command = commands[0]

        numbers = re.findall(r'\d+', line)

        x1 = numbers[0]
        y1 = numbers[1]
        x2 = numbers[2]
        y2 = numbers[3]

        for a in range(int(x1), int(x2)+1):
            for b in range(int(y1), int(y2)+1):
                if x1+'/'+y1 in t1:
                    t2[t1.index(x1+'/'+y1)] = setBool(command, t2[t1.index(x1+'/'+y1)])
                else:
                    t1.append(x1+'/'+y1)
                    t2[t1.index(x1+'/'+y1)] = setBool(command, t2[t1.index(x1+'/'+y1)])

print(len(t1))
c, t, f = 0, 0, 0
while c<len(t1):
    if t2[c] == True: t+=1
    else: f+=1
    c+=1
print('c :', c, 't :', t, 'f :', f)
'''