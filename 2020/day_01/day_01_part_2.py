with open('2020/day_01/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

for i in range(len(lines)):
    for a in range(i+1, len(lines)):
        if str(2020-int((lines[i].split('\n'))[0])-int((lines[a].split('\n'))[0]))+'\n' in lines:
            print(2020-int((lines[i].split('\n'))[0])-int((lines[a].split('\n'))[0]),int((lines[i].split('\n'))[0]), int((lines[a].split('\n'))[0]))
            print(((2020-int((lines[i].split('\n'))[0]))-int((lines[a].split('\n'))[0]))*int((lines[i].split('\n'))[0])*int((lines[a].split('\n'))[0]))
            break