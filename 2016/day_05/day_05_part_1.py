import hashlib

ID = 'cxdnnyjw'
s, a = 0, 0
t = []

while a<8:
    result = (hashlib.md5(ID.encode()+str(s).encode())).hexdigest()
    if result[0:5].count('0') == 5:
        t.append(ID+str(s))
        s += 1
        a += 1
    else: s += 1

word = ''

for i in t:
    word += (hashlib.md5(i.encode())).hexdigest()[5]
print(word)