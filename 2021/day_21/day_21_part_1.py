with open('2021/day_21/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

t = []
for i in lines:
    t.append((i.split(': ')[1]).split('\n')[0])

def determine(a_1, a_2):
    b_1, b_2, c_1, c_2, i = 0, 0, 0, 0, 1
    while b_1 != 1000 and b_2 != 1000:
        if i%2 == 1:
            if b_1 == 0: pos_1 = (((i+1)*3)%100+a_1)%10 + 1
            else: pos_1 = (((i+1)*3)%100+pos_1-1)%10 + 1
            b_1 += pos_1
            i+=3
            c_1 += 1
            if b_1 == 1000: break
        if i%2 == 0:
            if b_2 == 0: pos_2 = (((i+1)*3)%100+a_2)%10 + 1
            else: pos_2 = (((i+1)*3)%100+pos_2-1)%10 + 1
            b_2 += pos_2
            i+=3
            c_2 += 1
            if b_2 == 1000: break
    return (c_1+c_2)*3*min(b_1,b_2)
print(determine(int(t[0])-1,int(t[1])-1))