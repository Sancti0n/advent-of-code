with open('2021/day_01/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

increase = 0
for i in range(len(lines)):
    if i>0:
        if int(lines[i])>int(lines[i-1]):
            increase+=1
print(increase)