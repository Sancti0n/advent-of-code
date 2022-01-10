with open('2021/day_14/list.txt', encoding="utf-8") as f:
    lines = f.readlines()

w = lines[0].split('\n')[0]
lines.remove(lines[0])
lines.remove(lines[0])

word = []
for i in range(len(w)):
    word.append(w[i])

for i in range(len(lines)):
    lines[i] = lines[i].split('\n')[0]

t = {}
for i in lines:
    t[i.split(' -> ')[0]] = i.split(' -> ')[1]

def numb(t):
    d = {}
    for x in t:
        if x in d: d[x] += 1
        else: d[x] = 1
    return d

def poly(word, count):
    b = 0
    while b<count:
        a = 0
        while a<len(word):
            if a+1<len(word):
                word.insert(a+1, t[word[a]+word[a+1]])
                a+=2
            else: a+=1
        b+=1
    return numb(word)

f = poly(word,10)
print(max(f.values())-min(f.values()))