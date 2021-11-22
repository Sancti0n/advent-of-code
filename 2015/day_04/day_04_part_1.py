import hashlib

value = 'ckczppom'
s = 0
result = ''

while result[0:5].count('0') != 5:
    result = (hashlib.md5(value.encode()+str(s).encode())).hexdigest()
    s+=1
print(s-1)