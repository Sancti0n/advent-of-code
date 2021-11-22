import hashlib

value = 'ckczppom'
s = 0
result = ''

while result[0:6].count('0') != 6:
    result = (hashlib.md5(value.encode()+str(s).encode())).hexdigest()
    s+=1
print(s-1)